import { Input } from "../components/ui/Input"
import { Button } from "../components/ui/Button";

import { Link } from "react-router";

export function Register() {
  return (
    <div className="flex flex-1 flex-col justify-center items-center before:absolute before:left-[30%] before:w-1/3 before:bg-[#1A215E] before:rotate-35 before:h-[calc(100%_+_999px)] before:-top-100 overflow-clip before:-z-10 relative z-10 rounded-lg text-white">

        <form className="self-center ring-3 ring-black w-[30%] bg-neutral-50 h-auto flex flex-col items-center gap-y-8 rounded-xl py-8 my-8">
            <h1 className="text-black font-semibold text-3xl leading-relaxed underline underline-offset-4">Registrate</h1>
            {/* <div className="h-[1px] bg-gradient-to-r w-10/12 to-transparent via-black from-transparent"></div> */}
            <Input type="email" placeholder="Correo" />
            <Input type="password" placeholder="Contraseña" />
            <Input type="text" placeholder="Semestre" />
            <Input type="text" placeholder="Numero de Documento" />
            <Input type="text" placeholder="Tipo de Documento" />
            <Input type="text" placeholder="Estado Civil" />
            <Button className="w-3/5">Registrarse</Button>
            <p className="text-black">¿Ya tienes una cuenta?{" "}<Link to="/Login" className="text-blue-700 hover:underline transition-colors duration-150 ease-in-out">Inicia Sesion</Link></p>

        </form>
    </div>
  )
}
