import { Info } from "../components/Info";
import { Card } from "../components/Card";

import { Link } from "react-router";


const planes = [
  {
    title: "📘 Préstamo Educativo Tradicional",
    description:
      "Ideal para financiar tu matrícula universitaria con tasas preferenciales y plazos de hasta 60 meses. Perfecto si buscas estabilidad y pagos fijos.",
    img: "https://img.freepik.com/vector-gratis/libros-prestamos-dinero-becas_603843-826.jpg",
    className: "bg-bluedark-900",
  },
  {
    title: "💼 Préstamo para Material Académico",
    description:
      "Financia tus libros, equipos tecnológicos o herramientas de estudio con desembolsos rápidos y flexibles.",
      img: "https://img.freepik.com/vector-gratis/libros-prestamos-dinero-becas_603843-826.jpg",
    className: "bg-amber-800",
  },
  {
    title: "🕓 Préstamo a Corto Plazo",
    description:
      "Cubre gastos inmediatos como inscripciones, uniformes o certificaciones con plazos menores a 12 meses y trámites rápidos.",
      img: "https://img.freepik.com/vector-gratis/libros-prestamos-dinero-becas_603843-826.jpg",
    className: "bg-neutral-500",
  },
  {
    title: "🧩 Préstamo Integral",
    description:
      "Combina matrícula, manutención y transporte en un solo crédito. Ideal para quienes estudian lejos de casa o a tiempo completo.",
      img: "https://img.freepik.com/vector-gratis/libros-prestamos-dinero-becas_603843-826.jpg",
    className: "bg-green-700",
  },
  {
    title: "🌍 Préstamo para Estudios en el Exterior",
    description:
      "Diseñado para estudiantes que desean cursar programas fuera del país. Incluye opciones de periodo de gracia mientras estudias.",
      img: "https://img.freepik.com/vector-gratis/libros-prestamos-dinero-becas_603843-826.jpg",
    className: "bg-blue-900",
  },
];

import { useEffect, useMemo, useState } from "react";

export function Main() {
  //Utilizamos un hook para almacenar la lista sin perderse entre renders
  const [lista, setLista] = useState(planes);

  useEffect(() => {

  //creamos un intervalo que se ejecutara ciclicamente
  const interval = setInterval(() => {

    //Actualizamos la lista en cada ciclo
    setLista((prevLista) => {
      const newLista = prevLista.map((plan, i) => {

        //limpiamos cualquier animación vieja que haya quedado dentro de plan.className
        let newClass = plan.className.replace(" animate-fade-out-left", "").replace(" animate-fade-in-right", "");

        //Dependiendo del indice aplicamos las animaciones
        i === 2 ? newClass += " animate-fade-out-left" : "";
        i === 3 ? newClass += " animate-fade-in-right" : "";
        i === 1 ? newClass += " animate-slice-left" : "";
        i === 4 ? newClass += " animate-slice-right" : "";

        //Retornamos el objeto actualizado
        return { ...plan, className: newClass };
      });

      //retornamos la lista con las nuevas animaciones para que sean
      return newLista;
    });
    
    //Esperamos antes de cambiar la lista, dandole tiempo a que se visualicen las animaciones
    setTimeout(() => {
      setLista((prevLista) => {

        //Copiamos la lista actual y borramos su primer elemento para llevarlo al final de la fila
        const newLista = [...prevLista];
        const primero = newLista.shift();
        newLista.push(primero);

        //Recorremos la lista para limpiar cualquier animacion residual que haya quedado
        newLista.forEach((plan) => { plan.className = plan.className.replace(" animate-fade-out-left", "").replace(" animate-fade-in-right", "").replace(" animate-slice-left", "").replace(" animate-slice-right", ""); });

        //Actualizamos la lista y se repite el ciclo
        return newLista;
      });
    }, 2000);
  }, 6000);

  //Cuando se desmonta el componente, se limpia el intervalo
  return () => clearInterval(interval);
}, [ ]);

  const cards = useMemo(() => ( 
    lista.map((plan, index) => (
          <Card
          key={`${index}-${plan.title}`}
            title={plan.title}
            img={plan.img || null}
            className={`w-1/3 h-10/12 ${
              index === 2
                ? ""
                : `opacity-80 scale-70 ${
                    index === 0 || index === 4 ? "absolute translate-x-[250%] bottom-0" : ""
                  }`
            } ${plan.className}`}
          >
            {plan.description}
          </Card>
        ))
  ), [lista]);

  return (
    <>
      <div className="flex py-5 justify-start flex-wrap h-[100vh] border-b-2 bg-[#0e104c] border-[#1A215E] items-start">
        <img
          className="w-2/5 h-full object-contain shadow-amber-400 z-20 drop-shadow-2xl drop-shadow-blue-900"
          src="/Unilasallista_v3.png"
          alt="Imagen de inicio"
          />
      <Info /> 
      </div>


      <div className="relative w-full min-h-[100vh] h-[100vh] flex flex-1 [&>*]:cursor-default items-end justify-center">
        {cards}
      </div>
      <footer className="bg-[#1A215E] text-white text-center px-8 py-6 mt-16 flex justify-between ">
        <span className="mr-4 hover:text-blue-400 font-semibold transition-colors duration-300 ease-in-out">
          &copy; {new Date().getFullYear()} Coopla. Todos los derechos reservados.
        </span>
        <span>
          <Link to="/Contact" className="ml-4 hover:text-blue-400 font-semibold transition-colors duration-300 ease-in-out">
            Contactanos
          </Link>
        </span>
      </footer>
    </>
  );
}
