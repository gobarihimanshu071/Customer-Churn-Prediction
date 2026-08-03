import { useEffect, useState } from "react";
import API from "../services/api";

function PredictionHistory() {
  const [predictions, setPredictions] = useState([]);

  useEffect(() => {
    fetchPredictions();
  }, []);

  const fetchPredictions = async () => {
    try {
      const response = await API.get("/predictions");
      setPredictions(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 mt-8">

      <h2 className="text-2xl font-bold mb-6">
        Prediction History
      </h2>

      <table className="w-full border-collapse">

        <thead>

          <tr className="bg-gray-100">

            <th className="border p-3">ID</th>
            <th className="border p-3">Gender</th>
            <th className="border p-3">Prediction</th>
            <th className="border p-3">Probability</th>

          </tr>

        </thead>

        <tbody>

          {predictions.map((item) => (

            <tr key={item.id}>

              <td className="border p-3 text-center">
                {item.id}
              </td>

              <td className="border p-3 text-center">
                {item.gender}
              </td>

              <td
                className={`border p-3 text-center font-bold ${
                  item.prediction === "Yes"
                    ? "text-red-600"
                    : "text-green-600"
                }`}
              >
                {item.prediction}
              </td>

              <td className="border p-3 text-center">
                {(item.churn_probability * 100).toFixed(2)}%
              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default PredictionHistory;