
/
EntityObjects:
    
    ParkingSpot
        id : Integer
        vehicle : Vehicle
        isEmpty : Boolean

    TwoWheelerParkingSpot extend ParkingSpot
    LMVParkingSpot extend ParkingSpot
    HMVParkingSpot extend ParkingSpot
    Electric extend ParkingSpot

    ParkingSpotType(TWO_WHEELER, LMV, ELECTRIC, HMV)

    ParkingFloor
        id : Integer
        parkingSpots: List<ParkingSpot>
        entryGate: List<EntryGate>
        exitGate: List<ExitGate

    Vehicle
        id: string
        vehicleNo: string
        color: string

    VehicleType(TWO_WHEELER, LMV, ELECTRIC, HMV)

    Ticket
        id: string
        vehicle: Vehicle
        parkingSpot: ParkingSpot

    EntryGate
        gateId

    ExitGate
        gateId

    DisplayBoard
    PaymentProcess

/