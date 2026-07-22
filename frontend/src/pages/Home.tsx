"use client";

import { Clock, ExternalLink, Navigation, Star } from "lucide-react";
import {Map, MapMarker, MarkerContent, MarkerLabel, MarkerPopup} from "../components/mapcn-marker-popup.tsx";

const places = [
    {
        id: 1,
        name: "New York",
        label: "USA",
        category: "North America",
        rating: 4.9,
        reviewLabel: "Global City",
        hours: "24/7",
        image:
            "https://images.unsplash.com/photo-1496588152823-86ff7695e68f?w=300&h=200&fit=crop",
        lng: -74.006,
        lat: 40.7128,
    },
    {
        id: 2,
        name: "London",
        label: "UK",
        category: "Europe",
        rating: 4.9,
        reviewLabel: "Global City",
        hours: "24/7",
        image:
            "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=300&h=200&fit=crop",
        lng: -0.1278,
        lat: 51.5074,
    },
    {
        id: 3,
        name: "Paris",
        label: "France",
        category: "Europe",
        rating: 4.8,
        reviewLabel: "Global City",
        hours: "24/7",
        image:
            "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=300&h=200&fit=crop",
        lng: 2.3522,
        lat: 48.8566,
    },
    {
        id: 4,
        name: "Tokyo",
        label: "Japan",
        category: "Asia",
        rating: 4.9,
        reviewLabel: "Global City",
        hours: "24/7",
        image:
            "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=300&h=200&fit=crop",
        lng: 139.6917,
        lat: 35.6895,
    },
    {
        id: 5,
        name: "Singapore",
        label: "Singapore",
        category: "Asia",
        rating: 4.8,
        reviewLabel: "Global City",
        hours: "24/7",
        image:
            "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?w=300&h=200&fit=crop",
        lng: 103.8198,
        lat: 1.3521,
    },
    {
        id: 6,
        name: "Dubai",
        label: "UAE",
        category: "Middle East",
        rating: 4.8,
        reviewLabel: "Global City",
        hours: "24/7",
        image:
            "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=300&h=200&fit=crop",
        lng: 55.2708,
        lat: 25.2048,
    },
    {
        id: 7,
        name: "Mumbai",
        label: "India",
        category: "Asia",
        rating: 4.7,
        reviewLabel: "Global City",
        hours: "24/7",
        image:
            "https://images.unsplash.com/photo-1595658658481-d53d3f999875?w=300&h=200&fit=crop",
        lng: 72.8777,
        lat: 19.076,
    },
    {
        id: 8,
        name: "Sydney",
        label: "Australia",
        category: "Oceania",
        rating: 4.8,
        reviewLabel: "Global City",
        hours: "24/7",
        image:
            "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?w=300&h=200&fit=crop",
        lng: 151.2093,
        lat: -33.8688,
    },
    {
        id: 9,
        name: "São Paulo",
        label: "Brazil",
        category: "South America",
        rating: 4.7,
        reviewLabel: "Global City",
        hours: "24/7",
        image:
            "https://images.unsplash.com/photo-1543059080-f9b1272213d5?w=300&h=200&fit=crop",
        lng: -46.6333,
        lat: -23.5505,
    },
    {
        id: 10,
        name: "Cape Town",
        label: "South Africa",
        category: "Africa",
        rating: 4.8,
        reviewLabel: "Global City",
        hours: "24/7",
        image:
            "https://images.unsplash.com/photo-1576485375217-d6a95e34d043?w=300&h=200&fit=crop",
        lng: 18.4241,
        lat: -33.9249,
    },
];

export default function MarkerPopupDemo() {
    return (
        <div className="flex min-h-screen w-full items-center justify-center overflow-hidden bg-background p-8">
            <div className="h-[500px] w-full max-w-4xl overflow-hidden rounded-lg border bg-background shadow-sm">
                <Map center={[0, 20]}
                     zoom={1.8}>
                    {places.map((place) => (
                        <MapMarker key={place.id} longitude={place.lng} latitude={place.lat}>
                            <MarkerContent>
                                <div data-mapcn-rich-marker={place.name} className="size-5 cursor-pointer rounded-full border-2 border-white bg-rose-500 shadow-lg transition-transform hover:scale-110" />
                                <MarkerLabel position="bottom">{place.label}</MarkerLabel>
                            </MarkerContent>
                            <MarkerPopup className="w-62 p-0">
                                <div className="relative h-32 overflow-hidden rounded-t-md">
                                    <img src={place.image} alt={place.name} className="h-full w-full object-cover" />
                                </div>
                                <div className="space-y-2 p-3">
                                    <div>
                                        <p className="text-muted-foreground pb-0.5 text-[11px] font-medium tracking-wide uppercase">
                                            {place.category}
                                        </p>
                                        <h3 className="text-foreground leading-tight font-semibold">{place.name}</h3>
                                    </div>
                                    <div className="flex items-center gap-3 text-sm">
                                        <div className="flex items-center gap-1">
                                            <Star className="size-3.5 fill-amber-400 text-amber-400" />
                                            <span className="font-medium">{place.rating}</span>
                                            <span className="text-muted-foreground">({place.reviewLabel})</span>
                                        </div>
                                    </div>
                                    <div className="text-muted-foreground flex items-center gap-1.5 text-sm">
                                        <Clock className="size-3.5" />
                                        <span>{place.hours}</span>
                                    </div>
                                    <div className="flex gap-2 pt-1">
                                        <button className="inline-flex h-8 flex-1 items-center justify-center gap-1.5 rounded-md bg-primary px-3 text-sm font-medium text-primary-foreground shadow-sm transition-colors hover:bg-primary/90">
                                            <Navigation className="size-3.5" />
                                            Directions
                                        </button>
                                        <button className="inline-flex h-8 w-8 items-center justify-center rounded-md border border-input bg-background text-sm shadow-sm transition-colors hover:bg-accent hover:text-accent-foreground">
                                            <ExternalLink className="size-3.5" />
                                        </button>
                                    </div>
                                </div>
                            </MarkerPopup>
                        </MapMarker>
                    ))}
                </Map>
            </div>
        </div>
    );
}

export { MarkerPopupDemo };
