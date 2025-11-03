import { Button } from "../components/ui/Button";

import { useEffect, useState } from "react"

const planes = [
  {
    title: "Plan No 0",
    description: "Ideal para quienes están comenzando su aventura financiera. Ofrece tasas de interés competitivas y plazos flexibles para préstamos personales y comerciales.",
    link: "planno",
    img: "https://img.freepik.com/vector-gratis/libros-prestamos-dinero-becas_603843-826.jpg",
  },
  {
    title: "Plan Premium 1",
    description: "Ideal para quienes están comenzando su aventura financiera. Ofrece tasas de interés competitivas y plazos flexibles para préstamos personales y comerciales.",
    link: "planpremium",
    img: "https://img.freepik.com/vector-gratis/libros-prestamos-dinero-becas_603843-826.jpg",
  },
  {
    title: "Plan Básico 2",
    description: "Ideal para quienes están comenzando su aventura financiera. Ofrece tasas de interés competitivas y plazos flexibles para préstamos personales y comerciales.",
    link: "planbasico",
    img: "https://img.freepik.com/vector-gratis/libros-prestamos-dinero-becas_603843-826.jpg",
  }

]

export function Credits() {

  const [cont, setCont] = useState(0);
  const [objeto, setObjeto ] = useState(planes[0]);

  useEffect(() => {
     const intervalo = setInterval(() => {
       setCont(prev => { 
      const next = prev === planes.length-1 ? 0 : prev + 1;
      setObjeto(planes[next]);
      return next;
     } );
    }, 10000);

    return () => clearInterval(intervalo);
  }, [ ]);

  return (
    <>
      <div className="w-full flex flex-col flex-1 p-8 justify-center items-center">
        <article className="justify-center w-10/12 items-center flex flex-col space-y-8">
          <h2 className="font-bold text-2xl self-start text-bluedark-800">{objeto.title}</h2>
          <p className="text-lg leading-relaxed tracking-wide">{objeto.description}</p>
          <Button to={`${objeto.link}`} className="">Solicitar este Credito</Button>
          <img src={objeto.img} alt="" className="object-cover scale-50 hidden" />
        </article>        
        {cont}
      </div>
    </>
  );
}
