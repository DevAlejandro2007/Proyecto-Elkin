import { Banner } from "./components/Banner";
import { Info } from "./components/Info";

export default function App() {
  return (
    <div className="flex flex-1 flex-col w-full min-h-screen bg-neutral-50">
      <Banner title="Coopla" />

      <Info />
    </div>
  );
}
