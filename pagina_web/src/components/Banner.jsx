import { Menu } from "lucide-react";

export function Banner({title="Coopla"}) {
  return (
    <div className="w-full flex bg-fuchsia-900 text-white items-center p-6 min-h-[100px] max-h-[200px]">
        <Menu className="w-8 h-8 mr-4 hover:text-blue-700 transition-colors duration-300 ease-in-out cursor-pointer"/>
        <h1 className="font-bold text-4xl italic hover:text-blue-700 transition-colors duration-300 ease-in-out cursor-default">{title}</h1>
    </div>
  )
}
