export function Button({children}) {
  return (
    <button className="rounded-xl focus:outline-none bg-fuchsia-700 px-4 py-3 w-1/3 h-full hover:bg-fuchsia-600 transition-colors duration-300 ease-in-out hover:text-white">{children}</button>
  )
}
