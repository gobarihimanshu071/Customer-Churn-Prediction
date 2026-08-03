import Navbar from "../components/Navbar";
import CustomerForm from "../components/CustomerForm";
import PredictionCard from "../components/PredictionCard";

function Home() {
  return (
    <div className="min-h-screen bg-slate-100">

      <Navbar />

      <div className="max-w-7xl mx-auto p-8">

        <div className="grid lg:grid-cols-3 gap-8">

          {/* Left Side */}

          <div className="lg:col-span-2">

            <CustomerForm />

          </div>

          {/* Right Side */}

          <div>

            <PredictionCard />

          </div>

        </div>

      </div>

    </div>
  );
}

export default Home;