function PredictionCard({ result }) {

  if (!result) {
    return (
      <div className="bg-white rounded-xl shadow-lg p-6 sticky top-6">

        <h2 className="text-2xl font-bold mb-6">
          Prediction Result
        </h2>

        <div className="text-center">

          <div className="text-6xl">📊</div>

          <h3 className="mt-4 text-xl font-semibold">
            Waiting for Prediction
          </h3>

        </div>

      </div>
    );
  }

  const highRisk = result.prediction === "Yes";

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 sticky top-6">

      <h2 className="text-2xl font-bold mb-6">
        Prediction Result
      </h2>

      <div
        className={`rounded-xl p-6 ${
          highRisk ? "bg-red-100" : "bg-green-100"
        }`}
      >

        <h2 className="text-3xl font-bold">

          {highRisk ? "🔴 High Risk" : "🟢 Low Risk"}

        </h2>

        <p className="mt-4 text-lg">

          <strong>Status:</strong>{" "}
          {highRisk ? "Likely to Churn" : "Likely to Stay"}

        </p>

        <p className="mt-3 text-lg">

          <strong>Probability:</strong>{" "}
          {(result.churn_probability * 100).toFixed(2)}%

        </p>

      </div>

    </div>
  );
}

export default PredictionCard;