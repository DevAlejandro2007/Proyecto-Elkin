import { Link } from "react-router";

export function Button({children, className, to=null, ...props}) {

  return to ? (
    <Link to ={to} className={`rounded-xl focus:outline-none bg-[#1A215E] px-4 py-3 h-auto w-fit hover:bg-fuchsia-100 hover:ring-2 hover:ring-black transition-colors duration-300 ease-in-out hover:text-blue-800 text-white text-lg font-medium ${className}`} {...props}>{children}</Link>
  ) : (
    <button className={`rounded-xl focus:outline-none bg-[#1A215E] px-4 py-3 h-auto w-fit hover:bg-fuchsia-100 hover:ring-2 hover:ring-black transition-colors duration-300 ease-in-out hover:text-blue-800 text-white text-lg font-medium ${className}`} {...props}>{children}</button>
  )
}
