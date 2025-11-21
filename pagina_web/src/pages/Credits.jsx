import { Input } from "../components/ui/Input";
import { Button } from "../components/ui/Button";
import { H2 } from "../components/ui/H2";

import { useState } from "react";

import { Link } from "react-router-dom";

import { upForm } from "../utils/upForm";

export function Credits() {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    document: "",
    semestre: "",
    typeDocument: "",
    estadoCivil: "",
    typeCredit: "",
  });

  const handleUp = (e) => {
    e.preventDefault();

    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });

    console.table(formData);
  };

  return (
    <div className="flex flex-1 lg:justify-end justify-center items-center lg:before:absolute lg:before:left-[30%] lg:before:w-1/3 lg:before:bg-bluedark-900 lg:before:rotate-35 lg:before:h-[calc(100%_+_999px)] lg:before:-top-100 overflow-clip before:-z-10 relative z-10">
      <form
        className="lg:w-2/5 w-full bg-neutral-50 h-full flex flex-col items-start justify-center gap-y-8 py-8 px-12"
        onSubmit={upForm}
      >
        <H2>
          Solicita tu Credito
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
          name="typeCredit"
          value={formData.typeCredit}
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
        <p className="text-black">
          ¿Ya tienes una cuenta?{" "}
          <Link
            to="/Login"
            className="text-blue-700 hover:underline transition-colors duration-150 ease-in-out"
          >
            Inicia Sesion
          </Link>
        </p>
      </form>
    </div>
  );
}
