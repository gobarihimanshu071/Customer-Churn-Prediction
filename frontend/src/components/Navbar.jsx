function Navbar() {
  return (
    <nav className="bg-blue-700 shadow-lg">
      <div className="max-w-7xl mx-auto px-8 py-5 flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-white">
            Customer Churn Prediction
          </h1>
          <p className="text-blue-100">
            Telecom Customer Retention Dashboard
          </p>
        </div>

        <div className="text-white font-medium">
          FastAPI • React • AWS
        </div>
      </div>
    </nav>
  );
}

export default Navbar;