// src/App.jsx
import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [data, setData] = useState([]);
  const [filtered, setFiltered] = useState([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(false);

  const fetchData = async () => {
    setLoading(true);
    try {
      const res = await axios.get("http://localhost:5050/api/data");
      setData(res.data);
      setFiltered(res.data);
    } catch (err) {
      console.error("Erreur de chargement des données", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleSearch = (e) => {
    const value = e.target.value;
    setSearch(value);
    const result = data.filter((item) =>
      item.marque?.toLowerCase().includes(value.toLowerCase()) ||
      item.modele?.toLowerCase().includes(value.toLowerCase())
    );
    setFiltered(result);
  };

  return (
    <div className="p-4 font-sans">
      <h1 className="text-2xl font-bold mb-4">SmartScraper - Liste des armes</h1>

      <input
        type="text"
        value={search}
        onChange={handleSearch}
        placeholder="🔍 Rechercher une marque ou un modèle"
        className="p-2 border border-gray-300 rounded mb-4 w-full"
      />

      {loading ? (
        <p>Chargement en cours...</p>
      ) : (
        <div className="overflow-x-auto">
          <table className="table-auto w-full border">
            <thead className="bg-gray-200">
              <tr>
                <th className="p-2 border">Ref</th>
                <th className="p-2 border">Famille</th>
                <th className="p-2 border">Type</th>
                <th className="p-2 border">Marque</th>
                <th className="p-2 border">Modèle</th>
                <th className="p-2 border">Pays</th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((row, idx) => (
                <tr key={idx} className="hover:bg-gray-100">
                  <td className="p-2 border">{row.referenceRGA}</td>
                  <td className="p-2 border">{row.famille}</td>
                  <td className="p-2 border">{row.typeArme}</td>
                  <td className="p-2 border">{row.marque}</td>
                  <td className="p-2 border">{row.modele}</td>
                  <td className="p-2 border">{row.paysFabricant}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default App;