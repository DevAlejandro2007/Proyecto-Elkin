export function Button({children}) {
  return (
    <button className="rounded-xl focus:outline-none bg-fuchsia-700 px-4 py-3 w-1/3 h-full hover:bg-fuchsia-100 hover:ring-2 hover:ring-black transition-colors duration-300 ease-in-out hover:text-blue-800 text-white text-lg font-medium">{children}</button>
  )
}
