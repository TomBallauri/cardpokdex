import Header from "./components/Header.jsx";
import Footer from "./components/Footer.jsx";
import ApiTest from "./components/ApiTest.jsx";
import CardImage from "./components/CardImage.jsx";
import SetImage from "./components/SetImage.jsx";

export default function App() {
  return (
    <div>
      <Header />
      <main className="p-4 min-h-screen bg-white">
        {/* Section des Sets */}
        <section className="mb-12">
          <h1 className="text-4xl font-bold mb-6 text-purple-700">📦 Ensembles (Sets)</h1>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <SetImage setId="rsv10pt5" />
            <SetImage setId="zsv10pt5" />
          </div>
        </section>

        {/* Séparateur */}
        <hr className="my-12 border-t-2 border-gray-300" />

        {/* Section des Cartes */}
        <section>
          <h2 className="text-4xl font-bold mb-6 text-yellow-700">🎴 Galerie de Cartes</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <CardImage cardId="rsv10pt5-1" />
            <CardImage cardId="rsv10pt5-2" />
            <CardImage cardId="rsv10pt5-3" />
            <CardImage cardId="zsv10pt5-1" />
            <CardImage cardId="rsv10pt5-5" />
          </div>
        </section>
      </main>
      <ApiTest />
      <Footer />
    </div>
  );
}
