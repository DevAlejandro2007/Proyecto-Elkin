import { Button } from "./ui/Button";

export function Info({className}) {
  return (
    <div className={`flex flex-1 items-center justify-center flex-col text-center p-8 gap-4 [&>p]:text-md [&>p]:text-gray-600 w-1/2 self-center mt-8 space-y-4 [&>p]:text-2xl ${className}`}>
      <h2 className="font-bold text-3xl">¡Saca tu credito con nosotros!</h2>
      <p>En Coopla puedes sacar un prestamo estudiantil en base a tus posibilidades y necesidades en minutos. Dale click al boton de solicitar un credito para más información.</p>
      <Button>Solicitar Credito</Button>
    </div>
  )
}
