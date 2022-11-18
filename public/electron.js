const { BrowserWindow, app } = require("electron");
const isDev = require("electron-is-dev");
const { ipcMain } = require("electron/main");
const path = require("path");
const spawner = require("child_process").spawn;

let win = null;
function createWindow() {
  win = new BrowserWindow({
    width: 600,
    height: 700,
    minWidth: 600,
    minHeight: 700,
    webPreferences: {
      nodeIntegration: true,
      enableRemoteModule: true,
      contextIsolation: false,
      webSecurity: false,
    },
    title: false,
  });

  win.loadURL(
    isDev
      ? "http://localhost:3000"
      : `file://${path.join(__dirname, "../build/index.html")}`
  );
}

app.whenReady().then(createWindow);

//? IPCMAIN FUNCTION
ipcMain.on("recherche", (e, args) => {
  const { nodes, start, methode } = args;

  const python_process = spawner("python", [
    path.join(__dirname, "./engine/main.py"),
    nodes,
    start,
    methode,
  ]);

  python_process.stdout.on("data", (data) => {
    e.sender.send("recherche", data.toString());
  });
});
