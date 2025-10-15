import { Menu } from "lucide-react";

export function Banner({title="Coopla"}) {
  return (
    <div className="w-full flex bg-fuchsia-900 justify-between text-white items-center p-6 min-h-[100px] max-h-[200px]">
      <div className="w-1/2 h-full flex justify-start items-center self-center ">
        <Menu className="w-8 h-8 mr-4 hover:text-blue-700 transition-colors duration-300 ease-in-out cursor-pointer"/>
        <h1 className="font-bold text-4xl italic hover:text-blue-700 transition-colors duration-300 ease-in-out cursor-default">{title}</h1>
      </div>

      <div className="flex justify-end items-center gap-4 w-1/3 h-full">
        <button className="flex p-4 text-center justify-center items-center bg-fuchsia-950 hover:bg-fuchsia-50 text-white hover:text-blue-800 rounded-xl font-bold w-1/10 min-w-[200px] min-h-[50px] h-10/12 transition-colors duration-700 ease-in-out" >Creditos</button>
        <button className="flex p-4 text-center justify-center items-center bg-fuchsia-950 hover:bg-fuchsia-50 text-white hover:text-blue-800 rounded-xl font-bold w-1/10 min-w-[200px] min-h-[50px] h-10/12 transition-colors duration-700 ease-in-out" >Inicia Sesión</button>
      </div>

      
    </div>
  )
}
