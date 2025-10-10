import { Banner } from "./components/Banner";
import { Info } from "./components/Info";

export default function App() {
  return (
    <div className="flex flex-1 flex-col w-full h-screen bg-neutral-50 scroll-personalizada overflow-y-auto overflow-x-hidden pb-16">
      <Banner title="Coopla" />

      <div className="flex justify-around items-center gap-4 my-8 border-b-2 border-fuchsia-900 pb-8">
        <img className="w-10/12 h-128 object-cover bg-no-repeat " src="https://sial.educatic.com.co/appsFiles/archivosminerva/imgCartelera/empresa_1/FINANCIACI.N2024.07.25.13.30.14.png" alt="Imagen de banner" />
      </div>

      <Info />
    </div>
  );
}
