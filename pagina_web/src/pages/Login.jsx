import { Input } from "../components/ui/Input";
import { Button } from "../components/ui/Button";
import { H2 } from "../components/ui/H2";

import { Link } from "react-router-dom";
import { useState } from "react";

import { upForm } from "../utils/upForm"

export function Login() {

  const [ formData, setFormData ] = useState({
    email: "",
    password: "",
    confirmPassword: ""
  });

  const handleChange = (e) => {
    e.preventDefault();

    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });

    console.table(formData);
  };


  return (
    <div className="flex flex-1 flex-col justify-center items-end before:absolute before:left-[30%] before:w-2/5 before:bg-bluedark-900 before:rotate-35 before:h-[calc(100%_+_999px)] before:-top-100 overflow-clip before:-z-10 relative z-10">

        <form className="w-2/5 bg-neutral-50 h-full flex flex-col items-start justify-center gap-y-8 py-8 px-12" onSubmit={upForm}>
            <H2>Iniciar Sesión</H2>
            <Input type="email" placeholder="Correo" onChange={handleChange} />
            <Input type="password" placeholder="Contraseña" onChange={handleChange} />
            <Input type="password" placeholder="Confirma tu contraseña" onChange={handleChange} />
            <Button className="w-3/5" type="submit">Iniciar Sesión</Button>
            <p className="text-black">¿No tienes una cuenta?{" "}<Link to="/Register" className="text-blue-700 hover:underline transition-colors duration-150 ease-in-out">Registrate</Link></p>
        </form>
    </div>
  )
}
