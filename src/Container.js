import React from "react";
import "./App.css";

const { ipcRenderer } = window.require("electron");

export default function Container({ search, setSearch }) {
  const [methode, setMethod] = React.useState(1);
  const [nodes, setNodes] = React.useState("");
  const [start, setStart] = React.useState("");

  const submitHandler = () => {
    if (!nodes.length || !start.length) return;
    ipcRenderer.send("recherche", {
      nodes,
      start: parseInt(start),
      methode,
    });
  };

  return (
    <div>
      <div className="heading">
        <h1>DFS BFS Project M1</h1>
        <span>by MoumBou</span>
      </div>

      <div className="input_section">
        <h3>veillez introduire la liste des noeuds</h3>
        <textarea
          value={nodes}
          onChange={(e) => setNodes(e.target.value)}
          cols="30"
          rows="10"
          placeholder={` example
          [
            {1: 2},
            {1: 3},
            {2: 3},
            {2: 4},
            {3: 4},
            {4: 3}
        ]`}
        ></textarea>
        <div data-component="submit_section">
          <div>
            <label>donner le noeud de debut</label>
            <input
              type="text"
              value={start}
              onChange={(e) => setStart(e.target.value)}
            />
          </div>
          <div>
            <label>choisissez la methode de recherche</label>
            <div className="button_radio">
              <button
                onClick={() => {
                  setMethod(1);
                  setSearch([]);
                }}
                data-info={`${methode === 1 ? "selected" : ""}`}
              >
                DFS
              </button>
              <button
                onClick={() => {
                  setMethod(2);
                  setSearch([]);
                }}
                data-info={`${methode === 2 ? "selected" : ""}`}
              >
                BFS
              </button>
            </div>
          </div>
          <i></i>
          <div onClick={() => submitHandler()} data-component="submit">
            <button>confirmer</button>
          </div>
        </div>
      </div>

      <div data-component="result">
        {search ? (
          search.map((val, i) => {
            if (methode === 1 && i === 0)
              return (
                <>
                  <p>{start}</p>
                  <p>{val}</p>
                </>
              );
            return <p>{val}</p>;
          })
        ) : (
          <></>
        )}
      </div>
    </div>
  );
}
