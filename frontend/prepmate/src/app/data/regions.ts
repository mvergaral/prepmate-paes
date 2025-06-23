export interface Region {
  name: string;
  communes: string[];
}

export const REGIONS: Region[] = [
  {
    name: 'Región Metropolitana',
    communes: [
      'Cerrillos', 'Cerro Navia', 'Conchalí', 'El Bosque', 'Estación Central',
      'Huechuraba', 'Independencia', 'La Cisterna', 'La Florida', 'La Granja',
      'La Pintana', 'La Reina', 'Las Condes', 'Lo Barnechea', 'Lo Espejo',
      'Lo Prado', 'Macul', 'Maipú', 'Ñuñoa', 'Pedro Aguirre Cerda',
      'Peñalolén', 'Providencia', 'Pudahuel', 'Quilicura', 'Quinta Normal',
      'Recoleta', 'Renca', 'San Joaquín', 'San Miguel', 'San Ramón',
      'Santiago', 'Vitacura'
    ]
  },
  {
    name: 'Valparaíso',
    communes: [
      'Valparaíso', 'Viña del Mar', 'Concón', 'Quilpué', 'Villa Alemana'
    ]
  },
  {
    name: 'Biobío',
    communes: ['Concepción', 'Coronel', 'Talcahuano', 'Chiguayante']
  }
];
