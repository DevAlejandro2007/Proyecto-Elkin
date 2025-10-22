import { Banner } from "../components/Banner";
import { Info } from "../components/Info";
import { Card } from "../components/Card";

const planes = [
  {
    title: "📘 Préstamo Educativo Tradicional",
    description:
      "Ideal para financiar tu matrícula universitaria con tasas preferenciales y plazos de hasta 60 meses. Perfecto si buscas estabilidad y pagos fijos.",
    img: "https://img.freepik.com/vector-gratis/libros-prestamos-dinero-becas_603843-826.jpg",
    className: "hover:bg-neutral-900",
  },
  {
    title: "💼 Préstamo para Material Académico",
    description:
      "Financia tus libros, equipos tecnológicos o herramientas de estudio con desembolsos rápidos y flexibles.",
    className: "hover:bg-fuchsia-700",
  },
  {
    title: "🕓 Préstamo a Corto Plazo",
    description:
      "Cubre gastos inmediatos como inscripciones, uniformes o certificaciones con plazos menores a 12 meses y trámites rápidos.",
    className: "hover:bg-yellow-500",
  },
  {
    title: "🧩 Préstamo Integral",
    description:
      "Combina matrícula, manutención y transporte en un solo crédito. Ideal para quienes estudian lejos de casa o a tiempo completo.",
    className: "hover:bg-blue-600",
  },
  {
    title: "🌍 Préstamo para Estudios en el Exterior",
    description:
      "Diseñado para estudiantes que desean cursar programas fuera del país. Incluye opciones de periodo de gracia mientras estudias.",
    className: "hover:bg-green-700",
  },
];

import { useEffect, useState } from "react";

export function Main() {
  const [lista, setLista] = useState(planes);

  useEffect(() => {
  const interval = setInterval(() => {
    setLista((prevLista) => {
      const newLista = prevLista.map((plan, i) => {
        // Limpia cualquier animación previa
        let newClass = plan.className.replace(" animate-fade-out-left", "").replace(" animate-fade-in-right", "");

        i === 2 ? newClass += " animate-fade-out-left" : "";
        i === 3 ? newClass += " animate-fade-in-right" : "";
        i === 1 ? newClass += " animate-slice-left" : "";
        i === 4 ? newClass += " animate-slice-right" : "";
        return { ...plan, className: newClass };
      });
      return newLista;
    });

    // Luego, espera que termine la animación antes de rotar
    setTimeout(() => {
      setLista((prevLista) => {
        const newLista = [...prevLista];
        const primero = newLista.shift();
        newLista.forEach((plan) => { plan.className = plan.className.replace(" animate-fade-out-left", "").replace(" animate-fade-in-right", "").replace(" animate-slice-left", "").replace(" animate-slice-right", ""); });
        newLista.push(primero);
        return newLista;
      });
    }, 2000);
  }, 6000);

  return () => clearInterval(interval);
}, [ ]);


  return (
    <div className="flex flex-1 flex-col w-full h-screen bg-neutral-50 scroll-personalizada overflow-y-auto overflow-x-hidden">
      <Banner title="Coofla" />

      {/* <div className="flex justify-around items-center gap-4 my-8 border-b-2 border-fuchsia-900 p-8">
        <img
          className="w-10/12 h-128 object-cover bg-no-repeat"
          src="https://sial.educatic.com.co/appsFiles/archivosminerva/imgCartelera/empresa_1/FINANCIACI.N2024.07.25.13.30.14.png"
          alt="Imagen de inicio"
        />
      </div> */}

      <Info />
      <div className="relative min-h-[90vh] w-full flex my-6 [&>*]:cursor-default items-end justify-center">
        {lista.map((plan, index) => (
          <Card
            key={`${index}-${plan.title}-${Date.now()}`}
            title={plan.title}
            img={plan.img || null}
            className={`w-1/3 h-4/5 ${
              index === 2
                ? "[&>*]:text-black"
                : `[&>*]:text-black h-4/5 opacity-80 scale-70 ${
                    index === 0 || index === 4 ? "absolute translate-x-[250%]" : ""
                  }`
            } ${plan.className}`}
          >
            {plan.description}
          </Card>
        ))}
      </div>

      <footer
        className={`bg-fuchsia-900 flex justify-between w-full min-h-16 max-h-[10vh] items-center py-8 px-12 mt-24`}
      >
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
