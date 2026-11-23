"use strict";
const $ = (id) => document.getElementById(id);
const state = { all: [], area: "Todas", text: "", level: "", shown: 30 };
const STORAGE_KEY = "practica-asir-progres-v1";
let progress = {};
try { progress = JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}") || {}; } catch (_) { progress = {}; }
const clean = (text) => String(text || "").normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
const encodedPath = (path) => path.split("/").map(encodeURIComponent).join("/");
const sourceUrl = (path) => "https://github.com/jossanmar9/practica-asir/blob/main/" + encodedPath(path);
function saveProgress() { try { localStorage.setItem(STORAGE_KEY, JSON.stringify(progress)); } catch (_) {} }
function entryKey(entry) { return entry.path + (entry.id ? "#" + entry.id : ""); }
function statusFor(entry) { const value = progress[entryKey(entry)]; return value === "superat" || value === "completado" ? "completado" : "pendiente"; }
function card(entry) {
  const el = document.createElement("article");
  el.className = "exercise";
  const fileIcon = document.createElement("span");
  fileIcon.className = "file-icon";
  fileIcon.textContent = entry.area === "ASO" ? "SH" : entry.area === "Python" ? "PY" : "MD";
  el.appendChild(fileIcon);
  const main = document.createElement("div"); main.className = "exercise-main";
  const title = document.createElement("span"); title.className = "exercise-name"; title.textContent = entry.title;
  const meta = document.createElement("span"); meta.className = "exercise-meta";
  meta.textContent = entry.area + " · " + entry.unit + " · " + entry.level;
  main.append(title, meta); el.appendChild(main);
  const controls = document.createElement("div"); controls.className = "exercise-controls";
  const view = document.createElement("button"); view.type = "button"; view.textContent = "Enunciado";
  view.setAttribute("aria-label", "Consultar el enunciado de " + entry.title);
  view.addEventListener("click", () => showPreview(entry));
  const done = document.createElement("button"); done.type = "button";
  const status = statusFor(entry);
  done.textContent = status === "completado" ? "✓ Completado" : "○ Pendiente";
  done.classList.toggle("completed", status === "completado");
  done.setAttribute("aria-pressed", String(status === "completado"));
  done.addEventListener("click", () => {
    if (statusFor(entry) === "completado") delete progress[entryKey(entry)];
    else progress[entryKey(entry)] = "completado";
    saveProgress(); render();
  });
  controls.append(view, done); el.appendChild(controls);
  return el;
}
function filtered() {
  return state.all.filter((x) => (state.area === "Todas" || x.area === state.area)
    && (!state.level || x.level === state.level)
    && (!state.text || clean(x.path + " " + x.title + " " + x.unit + " " + x.area).includes(clean(state.text))));
}
function render() {
  const items = filtered();
  const parent = $("exercise-list"); parent.replaceChildren();
  const slice = items.slice(0, state.shown);
  if (!slice.length) {
    const empty = document.createElement("div"); empty.className = "empty";
    empty.textContent = "No hay ejercicios que coincidan con los filtros.";
    parent.appendChild(empty);
  }
  const fragment = document.createDocumentFragment();
  slice.forEach((entry) => fragment.appendChild(card(entry)));
  parent.appendChild(fragment);
  $("summary").textContent = items.length + " actividades encontradas · " + slice.length + " visibles";
  const passed = state.all.filter(x => statusFor(x) === "completado").length;
  $("progress").textContent = passed + " de " + state.all.length + " recursos completados";
  $("more").hidden = slice.length >= items.length;
}
async function showPreview(entry) {
  const dialog = $("preview");
  $("preview-title").textContent = entry.title;
  $("preview-type").textContent = entry.area + " · " + entry.unit + " · " + entry.level;
  $("preview-body").textContent = "Cargando enunciado…";
  $("preview-source").href = sourceUrl(entry.path);
  $("preview-download").href = encodedPath(entry.path);
  $("preview-download").setAttribute("download", entry.path.split("/").pop());
  if (!dialog.open) dialog.showModal();
  try {
    const result = await fetch(encodedPath(entry.path));
    if (!result.ok) throw Error("HTTP " + result.status);
    const text = await result.text();
    if (entry.id) {
      const marker = "## " + entry.id + " ";
      const start = text.indexOf(marker);
      const end = start < 0 ? -1 : text.indexOf("\n## UT", start + marker.length);
      $("preview-body").textContent = start < 0 ? text : text.slice(start, end < 0 ? undefined : end).trim();
    } else {
      $("preview-body").textContent = text;
    }
  } catch (_) {
    $("preview-body").textContent = "No se ha podido cargar el archivo. Puedes consultarlo en GitHub mediante el enlace inferior.";
  }
}
document.querySelectorAll("[data-filter-area]").forEach((button) => button.addEventListener("click", () => {
  state.area = button.dataset.filterArea;
  state.shown = 30;
  document.querySelectorAll("[data-filter-area]").forEach(x => x.classList.toggle("selected", x === button));
  render();
}));
document.querySelectorAll("[data-subject]").forEach((link) => link.addEventListener("click", () => {
  state.area = link.dataset.subject;
  state.shown = 30;
  document.querySelectorAll("[data-filter-area]").forEach(x => x.classList.toggle("selected", x.dataset.filterArea === state.area));
  render();
}));
$("search").addEventListener("input", (event) => { state.text = event.target.value; state.shown = 30; render(); });
$("level").addEventListener("change", (event) => { state.level = event.target.value; state.shown = 30; render(); });
$("more").addEventListener("click", () => { state.shown += 30; render(); });
$("export-progress").addEventListener("click", () => {
  if (!state.all.length) return;
  const rows = ["archivo,estado,intentos,nota,observaciones"];
  for (const entry of state.all) {
    rows.push([entryKey(entry), statusFor(entry), "", "", ""].join(","));
  }
  const blob = new Blob(["\ufeff" + rows.join("\n") + "\n"], { type: "text/csv;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = "seguimiento-asir.csv";
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
});
$("close-preview").addEventListener("click", () => $("preview").close());
$("preview").addEventListener("click", (event) => { if (event.target === $("preview")) $("preview").close(); });
(async () => {
  try {
    const response = await fetch("catalogo.json");
    if (!response.ok) throw Error("HTTP " + response.status);
    const entries = await response.json();
    if (!Array.isArray(entries)) throw Error("Formato de catálogo incorrecto");
    state.all = entries;
    render();
  } catch (_) {
    $("summary").textContent = "No se ha podido cargar el catálogo.";
    const a = document.createElement("a");
    a.href = "https://github.com/jossanmar9/practica-asir";
    a.textContent = "Consulta los ejercicios directamente en el repositorio.";
    $("exercise-list").replaceChildren(a);
  }
})();
