function Navbar() {
  return (
    <header className="bg-gradient-to-r from-blue-700 to-indigo-700 shadow-lg">
      <div className="max-w-7xl mx-auto px-8 py-6 flex justify-between items-center">

        <div>
          <h1 className="text-3xl font-bold text-white">
            Customer Churn Prediction
          </h1>

          <p className="text-blue-100 mt-1">
            Machine Learning Dashboard
          </p>
        </div>

        <div className="bg-white/20 px-4 py-2 rounded-lg text-white">
          React • FastAPI • AWS • MySQL
        </div>

      </div>
    </header>
  );
}

export default Navbar;