import { Input } from "../components/ui/Input";
import { Button } from "../components/ui/Button";
import { H2 } from "../components/ui/H2";
import { P } from "../components/ui/P";

import { useState } from "react";

import { Link } from "react-router";

import { upForm } from "../utils/upForm";

export function Register() {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    document: "",
    semestre: "",
    typeDocument: "",
    estadoCivil: "",
  });

  const handleUp = (e) => {
    e.preventDefault();

    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <div className="flex flex-1 justify-end items-center before:absolute before:left-[30%] before:w-1/3 before:bg-bluedark-900 before:rotate-35 before:h-[calc(100%_+_999px)] before:-top-100 overflow-clip before:-z-10 relative z-10">
      <form
        className="w-2/5 bg-neutral-50 h-full flex flex-col items-start justify-center gap-y-8 py-8 px-12"
        onSubmit={upForm}
      >
        <H2>
          Registrate
        </H2>
        <Input
          type="email"
          name="email"
          value={formData.email}
          onChange={handleUp}
          placeholder="Correo"
        />
        <Input
          type="password"
          name="password"
          value={formData.password}
          onChange={handleUp}
          placeholder="Contraseña"
        />
        <Input
          type="text"
          name="semestre"
          value={formData.semestre}
          onChange={handleUp}
          placeholder="Semestre"
        />
        <Input
          type="text"
          name="document"
          value={formData.document}
          onChange={handleUp}


          placeholder="Numero de Documento"
        />
        <Input
          type="text"
          name="typeDocument"
          value={formData.typeDocument}
          onChange={handleUp}
          placeholder="Tipo de Documento"
        />
        <Input
          type="text"
          name="estadoCivil"
          value={formData.estadoCivil}
          onChange={handleUp}
          placeholder="Estado Civil"
        />
        <Button className="w-3/5">Registrarse</Button>
        <P>
          ¿Ya tienes una cuenta?{" "}
          <Link
            to="/Login"
            className="text-blue-700 hover:underline transition-colors duration-150 ease-in-out"
          >
            Inicia Sesion
          </Link>
        </P>
      </form>
    </div>
  );
}
