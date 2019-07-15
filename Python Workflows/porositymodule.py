def porosity(Vp, Vt):
    phi = (Vp/Vt)*100 #multiply by 100 to get percent
    return phi

rock_1 = {
	"type": "sandstone",
	"Vp": 3,
	"Vt":75
}
	