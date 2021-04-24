@client.command()

async def scheda_cittadino(ctx, cittadino):
    if cittadino.disoccupato in Sì:
        await ctx.send(f"{cittadino.nome} {cittadino.cognome} vive in {cittadino.regione} ed è disoccupato")
        return f"{cittadino.nome} {cittadino.cognome} vive in {cittadino.regione} ed è disoccupato"
    if cittadino.disoccupato in No:
        await ctx.send(f"{cittadino.nome} {cittadino.cognome}: lavora come {cittadino.lavoro} per conto di {cittadino.datore_di_lavoro} con lo stipendio di {cittadino.reddito}€ al mese, residente in {cittadino.regione}")
        return f"{cittadino.nome} {cittadino.cognome}: lavora come {cittadino.lavoro} per conto di {cittadino.datore_di_lavoro} con lo stipendio di {cittadino.reddito}€ al mese, residente in {cittadino.regione}"
