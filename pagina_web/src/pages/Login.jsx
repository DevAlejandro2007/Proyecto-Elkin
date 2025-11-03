import { Input } from "../components/ui/Input";
import { Button } from "../components/ui/Button";

import { Link } from "react-router";

export function Login() {
  return (
    <div className="flex flex-1 flex-col justify-center items-center before:absolute before:left-[30%] before:w-1/3 before:bg-[#1A215E] before:rotate-35 before:h-[calc(100%_+_999px)] before:-top-100 overflow-clip before:-z-10 relative z-10 rounded-lg text-white">

        <form className="self-center ring-3 ring-black w-[30%] bg-neutral-50 h-auto flex flex-col items-center gap-y-8 rounded-xl py-8 my-8">
            <h1 className="text-black font-semibold text-3xl leading-relaxed underline underline-offset-4">Iniciar Sesión</h1>
            <Input type="email" placeholder="Correo" />
            <Input type="password" placeholder="Contraseña" />
            <Input type="password" placeholder="Confrima tu contraseña" />
            <Button className="w-3/5">Iniciar Sesión</Button>
            <p className="text-black">¿No tienes una cuenta?{" "}<Link to="/Register" className="text-blue-700 hover:underline transition-colors duration-150 ease-in-out">Registrate</Link></p>

        </form>
    </div>
  )
}
