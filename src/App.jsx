import Header from "./components/Header.jsx";
import Footer from "./components/Footer.jsx";
import ApiTest from "./components/ApiTest.jsx";
import CardImage from "./components/CardImage.jsx";
import SetImage from "./components/SetImage.jsx";
import AdminModif from "./pages/AdminModif.jsx";

export default function App() {
  const path = typeof window !== 'undefined' ? window.location.pathname : '/';

  // Simple client-side routing (no react-router dependency)
  if (path === '/admin') {
    return (
      <div>
        <Header />
        <main>
          <section>
            <AdminModif />
          </section>
        </main>
        <Footer />
      </div>
    );
  }

  // Default home page
  return (
    <div>
      <Header />
      <main>
        <section style={{ padding: 20 }}>
          <h1>Bienvenue — CardPokdex</h1>
          <p>
            Pour accéder au panneau d'administration, ouvrez <a href="/admin">/admin</a>
          </p>
        </section>
      </main>
      <Footer />
    </div>
  );
}
