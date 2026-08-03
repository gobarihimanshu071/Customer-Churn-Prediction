import { useState } from "react";
import API from "../services/api";

function CustomerForm({ setResult }) {
  const [formData, setFormData] = useState({
    gender: "Male",
    SeniorCitizen: 0,
    Partner: "Yes",
    Dependents: "No",
    tenure: 12,
    PhoneService: "Yes",
    MultipleLines: "No",
    InternetService: "Fiber optic",
    OnlineSecurity: "No",
    OnlineBackup: "No",
    DeviceProtection: "No",
    TechSupport: "No",
    StreamingTV: "Yes",
    StreamingMovies: "Yes",
    Contract: "Month-to-month",
    PaperlessBilling: "Yes",
    PaymentMethod: "Electronic check",
    MonthlyCharges: 95.25,
    TotalCharges: 1143,
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async () => {
    try {
      const response = await API.post("/predict", formData);
      setResult(response.data);
    } catch (error) {
      console.log(error);
      alert("Prediction failed");
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-md p-8 mt-8">
      <h2 className="text-3xl font-bold mb-2">
        Customer Information
      </h2>

      <p className="text-gray-500 mb-8">
        Enter the customer's telecom details.
      </p>

      <div className="grid grid-cols-2 gap-6">

        <div>
          <label className="block mb-2 font-medium">
            Gender
          </label>

          <select
            name="gender"
            value={formData.gender}
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
          >
            <option>Male</option>
            <option>Female</option>
          </select>
        </div>

        <div>
          <label className="block mb-2 font-medium">
            Tenure
          </label>

          <input
            type="number"
            name="tenure"
            value={formData.tenure}
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
          />
        </div>

        <div>
          <label className="block mb-2 font-medium">
            Monthly Charges
          </label>

          <input
            type="number"
            name="MonthlyCharges"
            value={formData.MonthlyCharges}
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
          />
        </div>

        <div>
          <label className="block mb-2 font-medium">
            Total Charges
          </label>

          <input
            type="number"
            name="TotalCharges"
            value={formData.TotalCharges}
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
          />
        </div>

      </div>

      <button
        onClick={handleSubmit}
        className="mt-8 bg-blue-700 text-white px-6 py-3 rounded-lg hover:bg-blue-800"
      >
        Predict Customer
      </button>
    </div>
  );
}

export default CustomerForm;