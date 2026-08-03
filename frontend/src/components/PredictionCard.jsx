function PredictionCard() {
  return (
    <div className="bg-white rounded-xl shadow-lg p-6 sticky top-6">

      <h2 className="text-2xl font-bold mb-6">
        Prediction Result
      </h2>

      <div className="border rounded-xl p-6">

        <div className="text-center">

          <div className="text-6xl mb-4">
            📊
          </div>

          <h3 className="text-xl font-semibold">
            Waiting for Prediction
          </h3>

          <p className="text-gray-500 mt-3">
            Fill the customer details and click
            <strong> Predict Customer</strong>.
          </p>

        </div>

      </div>

    </div>
  );
}

export default PredictionCard;