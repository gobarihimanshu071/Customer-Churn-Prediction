import Navbar from "../components/Navbar";
import CustomerForm from "../components/CustomerForm";

function Home() {
  return (
    <div className="min-h-screen bg-slate-100">

      <Navbar />

      <main className="max-w-6xl mx-auto py-10">

        <div className="bg-white rounded-xl shadow-md p-8">

          <h2 className="text-2xl font-semibold mb-3">
            Welcome 👋
          </h2>

          <p className="text-gray-600">
            This dashboard predicts whether a telecom customer is likely to churn
            using a Machine Learning model deployed on AWS.
          </p>

        </div>

        <CustomerForm />

      </main>

    </div>
  );
}

export default Home;