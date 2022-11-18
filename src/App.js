import React from "react";
import Container from "./Container";

const { ipcRenderer } = window.require("electron");

function App() {
  const [search, setSearch] = React.useState([]);

  ipcRenderer.on("recherche", (e, args) => {
    if (args) setSearch(JSON.parse(args));
  });

  return (
    <div>
      <Container search={search} setSearch={setSearch} />
    </div>
  );
}

export default App;
