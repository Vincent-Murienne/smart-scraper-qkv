import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [data, setData] = useState([]);
  const [search, setSearch] = useState("");
  const [famille, setFamille] = useState("");
  const [typeArme, setTypeArme] = useState("");
  const [page, setPage] = useState(1);
  const [total, setTotal] = useState(0);
  const limit = 10;

  const fetchData = async () => {
    try {
      const res = await axios.get("http://localhost:5050/api/armes", {
        params: {
          search,
          famille,
          typeArme,
          page,
          limit,
        },
      });
      setData(res.data.data);
      setTotal(res.data.total);
    } catch (err) {
      console.error("Erreur API", err);
    }
  };

  useEffect(() => {
    fetchData();
  }, [page]);

  const handleSearch = () => {
    setPage(1);
    fetchData();
  };

  const totalPages = Math.ceil(total / limit);

  return (
    <div className="p-4 max-w-7xl mx-auto font-sans">
      <h1 className="text-2xl font-bold mb-4">🔫 SmartScraper - Armes</h1>

      <div className="grid grid-cols-1 sm:grid-cols-4 gap-4 mb-4">
        <input
          type="text"
          placeholder="Rechercher..."
          className="p-2 border border-gray-300 rounded w-full"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <select
          className="p-2 border border-gray-300 rounded"
          value={famille}
          onChange={(e) => setFamille(e.target.value)}
        >
          <option value="">-- Famille --</option>
          <option value="épaule">Épaule</option>
          <option value="poing">Poing</option>
        </select>
        <select
          className="p-2 border border-gray-300 rounded"
          value={typeArme}
          onChange={(e) => setTypeArme(e.target.value)}
        >
          <option value="">-- Type d'arme --</option>
          <option value="carabine">Carabine</option>
          <option value="pistolet">Pistolet</option>
          <option value="fusil">Fusil</option>
        </select>
        <button
          onClick={handleSearch}
          className="bg-blue-600 text-white rounded px-4 py-2"
        >
          🔍 Rechercher
        </button>
      </div>

      <div className="overflow-x-auto">
        <table className="table-auto w-full border text-sm">
          <thead className="bg-gray-200">
            <tr>
              <th className="p-2 border">Réf</th>
              <th className="p-2 border">Famille</th>
              <th className="p-2 border">Type</th>
              <th className="p-2 border">Marque</th>
              <th className="p-2 border">Modèle</th>
              <th className="p-2 border">Pays</th>
            </tr>
          </thead>
          <tbody>
            {data.map((row, idx) => (
              <tr key={idx} className="hover:bg-gray-50">
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

      <div className="mt-4 flex justify-between items-center">
        <button
          disabled={page <= 1}
          onClick={() => setPage((p) => p - 1)}
          className="px-3 py-1 bg-gray-200 rounded disabled:opacity-50"
        >
          ← Précédent
        </button>
        <span>
          Page {page} / {totalPages}
        </span>
        <button
          disabled={page >= totalPages}
          onClick={() => setPage((p) => p + 1)}
          className="px-3 py-1 bg-gray-200 rounded disabled:opacity-50"
        >
          Suivant →
        </button>
      </div>
    </div>
  );
}

export default App;