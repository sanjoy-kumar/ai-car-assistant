import type { Car } from '../types/car';

interface Props {
  car: Car
  setCar: (car: Car) => void
}

function CarForm({ car, setCar }: Props) {
  return (
    <>
      <h3>Car Info</h3>

      <div className="car-info-grid">

        <input
          placeholder="Make"
          value={car.make}
          onChange={(e) =>
            setCar({ ...car, make: e.target.value })
          }
        />

        <input
          placeholder="Model"
          value={car.model}
          onChange={(e) =>
            setCar({ ...car, model: e.target.value })
          }
        />

        <input
          placeholder="Year"
          value={car.year}
          onChange={(e) =>
            setCar({ ...car, year: e.target.value })
          }
        />

        <input
          placeholder="Mileage"
          value={car.mileage}
          onChange={(e) =>
            setCar({ ...car, mileage: e.target.value })
          }
        />

      </div>
    </>
  )
}

export default CarForm
