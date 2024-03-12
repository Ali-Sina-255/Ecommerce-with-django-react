import { Container } from 'react-bootstrap'
import Header from "./components/Header";
import Footer from "./components/Footer";
import HomeScreen from './screen/HomeScreen';

function App() {
  return (
    <div className="py-3">
      <Header/>
      <main>
        <Container>
        <h1>Hello, world</h1>
        <HomeScreen/>
        </Container>
      </main>
      <Footer/>
    </div>
  );
}

export default App;
