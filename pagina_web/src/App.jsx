import { Banner } from "./components/Banner";
import { Info } from "./components/Info";
import { Card } from "./components/Card";

export default function App() {
  return (
    <div className="flex flex-1 flex-col w-full h-screen bg-neutral-50 scroll-personalizada overflow-y-auto overflow-x-hidden">
      <Banner title="Coopla" />

      <div className="flex justify-around items-center gap-4 my-8 border-b-2 border-fuchsia-900 p-8">
        <img
          className="w-10/12 h-128 object-cover bg-no-repeat"
          src="https://sial.educatic.com.co/appsFiles/archivosminerva/imgCartelera/empresa_1/FINANCIACI.N2024.07.25.13.30.14.png"
          alt="Imagen de inicio"
        />
      </div>

      <Info />
      <div className="h-auto w-full px-6 flex my-6 flex-wrap lg:justify-around sm:justify-center sm:gap-8 [&>*]:cursor-default items-start">
        <Card className="max-w-sm h-auto hover:bg-blue-800">
          <h2 className="text-lg font-semibold text-fuchsia-900 mb-2">
            📘 Préstamo Educativo Tradicional
          </h2>
          <p className="text-gray-700 leading-relaxed">
            Ideal para financiar tu matrícula universitaria con tasas preferenciales
            y plazos de hasta 60 meses. Perfecto si buscas estabilidad y pagos fijos.
          </p>
        </Card>

        <Card className="max-w-sm h-auto  hover:bg-fuchsia-700">
          <h2 className="text-lg font-semibold text-fuchsia-900 mb-2">
            💼 Préstamo para Material Académico
          </h2>
          <p className="text-gray-700 leading-relaxed">
            Financia tus libros, equipos tecnológicos o herramientas de estudio con
            desembolsos rápidos y flexibles.
          </p>
        </Card>


        <Card className="max-w-sm h-auto hover:bg-gray-600">
          <h2 className="text-lg font-semibold text-fuchsia-900 mb-2">
            🕓 Préstamo a Corto Plazo
          </h2>
          <p className="text-gray-700 leading-relaxed">
            Cubre gastos inmediatos como inscripciones, uniformes o certificaciones
            con plazos menores a 12 meses y trámites rápidos.
          </p>
        </Card>

        <Card className="max-w-sm h-auto hover:bg-emerald-700">
          <h2 className="text-lg font-semibold text-fuchsia-900 mb-2">
            🧩 Préstamo Integral
          </h2>
          <p className="text-gray-700 leading-relaxed">
            Combina matrícula, manutención y transporte en un solo crédito. Ideal
            para quienes estudian lejos de casa o a tiempo completo.
          </p>
        </Card>
        <Card className="max-w-sm h-auto hover:bg-green-800">
          <h2 className="text-lg font-semibold text-fuchsia-900 mb-2">
            🌍 Préstamo para Estudios en el Exterior
          </h2>
          <p className="text-gray-700 leading-relaxed">
            Diseñado para estudiantes que desean cursar programas fuera del país.
            Incluye opciones de periodo de gracia mientras estudias.
          </p>
        </Card>
      </div>

      <footer className={`bg-fuchsia-900 flex justify-between w-full min-h-16 max-h-[10vh] items-center py-8 px-12 mt-24`}>
        <span className="text-white font-medium hover:text-blue-800 text-xl transition-color duration-300 ease-in-out cursor-pointer">
          Contactanos
        </span>
        <span className="text-white font-medium hover:text-blue-800 text-xl transition-color duration-300 ease-in-out cursor-pointer">
          Terminos y condiciones
        </span>

        
      </footer>
    </div>
  );
}
