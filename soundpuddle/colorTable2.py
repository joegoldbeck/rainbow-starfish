colorTable = bytearray([
0x80,0x80,0x80,
0x80,0x81,0x80,
0x80,0x82,0x80,
0x80,0x83,0x80,
0x80,0x84,0x80,
0x80,0x85,0x80,
0x80,0x86,0x80,
0x80,0x87,0x80,
0x80,0x88,0x80,
0x80,0x89,0x80,
0x80,0x8a,0x80,
0x80,0x8b,0x80,
0x80,0x8c,0x80,
0x80,0x8d,0x80,
0x80,0x8e,0x80,
0x80,0x8f,0x80,
0x80,0x90,0x80,
0x80,0x91,0x80,
0x80,0x92,0x80,
0x80,0x93,0x80,
0x80,0x94,0x80,
0x81,0x95,0x80,
0x81,0x96,0x80,
0x81,0x97,0x80,
0x81,0x98,0x80,
0x81,0x99,0x80,
0x82,0x9a,0x80,
0x82,0x9b,0x80,
0x82,0x9c,0x80,
0x83,0x9d,0x80,
0x83,0x9e,0x80,
0x83,0x9f,0x80,
0x84,0xa0,0x80,
0x84,0xa0,0x80,
0x84,0xa1,0x80,
0x85,0xa2,0x80,
0x85,0xa3,0x80,
0x86,0xa4,0x80,
0x86,0xa5,0x80,
0x87,0xa6,0x80,
0x87,0xa7,0x80,
0x87,0xa8,0x80,
0x88,0xa9,0x80,
0x89,0xaa,0x80,
0x89,0xab,0x80,
0x8a,0xac,0x80,
0x8a,0xad,0x80,
0x8b,0xae,0x80,
0x8c,0xaf,0x80,
0x8c,0xb0,0x80,
0x8d,0xb1,0x80,
0x8d,0xb2,0x80,
0x8e,0xb3,0x80,
0x8f,0xb4,0x80,
0x8f,0xb5,0x80,
0x90,0xb6,0x80,
0x91,0xb7,0x80,
0x92,0xb8,0x80,
0x92,0xb9,0x80,
0x93,0xba,0x80,
0x94,0xbb,0x80,
0x95,0xbc,0x80,
0x95,0xbd,0x80,
0x96,0xbe,0x80,
0x97,0xbf,0x80,
0x98,0xc0,0x80,
0x99,0xc1,0x80,
0x99,0xc2,0x80,
0x9a,0xc3,0x80,
0x9b,0xc4,0x80,
0x9c,0xc5,0x80,
0x9d,0xc5,0x80,
0x9e,0xc6,0x80,
0x9f,0xc7,0x80,
0xa0,0xc8,0x80,
0xa1,0xc9,0x80,
0xa2,0xca,0x80,
0xa3,0xcb,0x80,
0xa4,0xcc,0x80,
0xa5,0xcd,0x80,
0xa6,0xce,0x80,
0xa7,0xcf,0x80,
0xa8,0xd0,0x80,
0xa9,0xd1,0x80,
0xaa,0xd2,0x80,
0xab,0xd3,0x80,
0xac,0xd4,0x80,
0xad,0xd5,0x80,
0xaf,0xd6,0x80,
0xb0,0xd7,0x80,
0xb1,0xd7,0x80,
0xb2,0xd8,0x80,
0xb3,0xd9,0x80,
0xb4,0xda,0x80,
0xb6,0xdb,0x80,
0xb7,0xdc,0x80,
0xb8,0xdd,0x80,
0xba,0xde,0x80,
0xbb,0xdf,0x80,
0xbc,0xe0,0x80,
0xbd,0xe1,0x80,
0xbf,0xe2,0x80,
0xc0,0xe3,0x80,
0xc2,0xe3,0x80,
0xc3,0xe4,0x80,
0xc4,0xe5,0x80,
0xc6,0xe6,0x80,
0xc7,0xe7,0x80,
0xc8,0xe8,0x80,
0xca,0xe9,0x80,
0xcb,0xea,0x80,
0xcc,0xeb,0x80,
0xce,0xec,0x80,
0xcf,0xed,0x80,
0xd1,0xed,0x80,
0xd2,0xee,0x80,
0xd3,0xef,0x80,
0xd4,0xf0,0x80,
0xd5,0xeb,0x80,
0xd5,0xeb,0x80,
0xd6,0xeb,0x80,
0xd7,0xea,0x80,
0xd7,0xea,0x80,
0xd8,0xea,0x80,
0xd8,0xe9,0x80,
0xd9,0xe9,0x80,
0xda,0xe9,0x80,
0xda,0xe8,0x80,
0xdb,0xe8,0x80,
0xdc,0xe7,0x80,
0xdd,0xe7,0x80,
0xdd,0xe6,0x80,
0xde,0xe6,0x80,
0xde,0xe5,0x80,
0xdf,0xe4,0x81,
0xdf,0xe3,0x82,
0xdf,0xe2,0x83,
0xdf,0xe1,0x83,
0xdf,0xe0,0x84,
0xdf,0xdf,0x85,
0xdf,0xde,0x86,
0xdf,0xdd,0x87,
0xdf,0xdc,0x88,
0xdf,0xdb,0x88,
0xdf,0xda,0x89,
0xdf,0xd9,0x8a,
0xdf,0xd8,0x8b,
0xdf,0xd8,0x8c,
0xdf,0xd7,0x8d,
0xdf,0xd6,0x8d,
0xdf,0xd5,0x8e,
0xdf,0xd4,0x8f,
0xdf,0xd4,0x90,
0xdf,0xd3,0x91,
0xdf,0xd2,0x92,
0xdf,0xd1,0x92,
0xdf,0xd0,0x93,
0xdf,0xd0,0x94,
0xdf,0xcf,0x95,
0xdf,0xce,0x96,
0xdf,0xce,0x96,
0xdf,0xcd,0x97,
0xdf,0xcc,0x98,
0xdf,0xcc,0x99,
0xdf,0xcb,0x9a,
0xdf,0xcb,0x9a,
0xdf,0xca,0x9b,
0xdf,0xc9,0x9c,
0xdf,0xc9,0x9d,
0xdf,0xc8,0x9e,
0xdf,0xc8,0x9e,
0xdf,0xc7,0x9f,
0xdf,0xc7,0xa0,
0xdf,0xc6,0xa1,
0xdf,0xc6,0xa2,
0xdf,0xc5,0xa2,
0xdf,0xc5,0xa3,
0xdf,0xc5,0xa4,
0xdf,0xc4,0xa5,
0xdf,0xc4,0xa5,
0xdf,0xc3,0xa6,
0xdf,0xc3,0xa7,
0xdf,0xc3,0xa8,
0xdf,0xc2,0xa8,
0xdf,0xc2,0xa9,
0xdf,0xc2,0xaa,
0xdf,0xc1,0xab,
0xdf,0xc1,0xab,
0xdf,0xc1,0xac,
0xdf,0xc1,0xad,
0xdf,0xc0,0xae,
0xdf,0xc0,0xae,
0xdf,0xc0,0xaf,
0xdf,0xc0,0xb0,
0xdf,0xbf,0xb0,
0xdf,0xbf,0xb1,
0xdf,0xbf,0xb2,
0xdf,0xbf,0xb3,
0xdf,0xbf,0xb3,
0xdf,0xbf,0xb4,
0xdf,0xbe,0xb5,
0xdf,0xbe,0xb5,
0xdf,0xbe,0xb6,
0xdf,0xbe,0xb7,
0xdf,0xbe,0xb8,
0xdf,0xbe,0xb8,
0xdf,0xbe,0xb9,
0xdf,0xbe,0xba,
0xdf,0xbe,0xba,
0xdf,0xbe,0xbb,
0xdf,0xbe,0xbc,
0xdf,0xbe,0xbc,
0xdf,0xbe,0xbd,
0xdf,0xbe,0xbe,
0xdf,0xbe,0xbf,
0xdf,0xbe,0xc0,
0xdf,0xbe,0xc2,
0xdf,0xc0,0xc3,
0xdf,0xc1,0xc4,
0xdf,0xc2,0xc5,
0xdf,0xc2,0xc7,
0xdf,0xc3,0xc8,
0xdf,0xc4,0xc9,
0xdf,0xc4,0xca,
0xdf,0xc5,0xcb,
0xdf,0xc5,0xcc,
0xdf,0xc6,0xcd,
0xdf,0xc7,0xcf,
0xdf,0xc7,0xd0,
0xdf,0xc8,0xd1,
0xdf,0xc9,0xd2,
0xdf,0xc9,0xd3,
0xdf,0xca,0xd4,
0xdf,0xca,0xd5,
0xdf,0xcb,0xd6,
0xdf,0xcc,0xd7,
0xdf,0xcc,0xd8,
0xdf,0xcd,0xd9,
0xdf,0xcd,0xda,
0xdf,0xce,0xdb,
0xdf,0xcf,0xdc,
0xdf,0xcf,0xdd,
0xdf,0xd0,0xdd,
0xdf,0xd0,0xde,
0xdf,0xd1,0xdf,
0xdf,0xd1,0xe0,
0xdf,0xd2,0xe1,
0xdf,0xd3,0xe2,
0xdf,0xd3,0xe3,
0xdf,0xd4,0xe3,
0xdf,0xd4,0xe4,
0xdf,0xd5,0xe5,
0xdf,0xd5,0xe6,
0xdf,0xd6,0xe6,
0xdf,0xd6,0xe7,
0xdf,0xd7,0xe8])
