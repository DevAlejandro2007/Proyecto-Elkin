import { BrowserRouter, Routes, Route } from "react-router";

import { Main } from "./pages/Main";
import { Login } from "./pages/Login";
import { Credits } from "./pages/Credits";
import { Pruebas } from "./pages/Pruebas";
import { Register } from "./pages/Register";

import { Banner } from "./components/Banner";

export default function App() {
  return (
    <BrowserRouter>
      <div className="flex flex-col h-screen min-h-0">

      <Banner title="Coofla" />
        <main className="flex flex-1 w-screen flex-col scroll-personalizada overflow-y-auto min-h-0 h-screen overflow-x-hidden">
          <Routes>
            <Route path="/" element={<Main></Main>} />
            <Route path="/Login" element={<Login></Login>} />
            <Route path="/Credits" element={<Credits></Credits>} />
            <Route path="/Register" element={<Register></Register>} />
            <Route path="/Pruebas" element={<Pruebas></Pruebas>} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}
