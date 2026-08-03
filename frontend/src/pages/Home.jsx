import { useState } from "react";
import Navbar from "../components/Navbar";
import CustomerForm from "../components/CustomerForm";
import PredictionCard from "../components/PredictionCard";
import PredictionHistory from "../components/PredictionHistory";
function Home() {

  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen bg-slate-100">

      <Navbar />

      <div className="max-w-7xl mx-auto p-8">

        <div className="grid lg:grid-cols-3 gap-8">

          <div className="lg:col-span-2">
            <CustomerForm setResult={setResult} />
          </div>

          

          <div>
            <PredictionCard result={result} />
          </div>

        </div>
        <div className="mt-8">
    <PredictionHistory />
</div>

      </div>

    </div>
  );
}

export default Home;