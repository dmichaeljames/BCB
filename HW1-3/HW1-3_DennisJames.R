d <- read.table("GenBank_YearlyGrowth.txt", header = TRUE)

# Convert BP to millions
mil <- function(a)
{
	return(a / 1000000)
}

# Convert sequences to thousands
thou <- function(a)
{
	return(a / 1000)
}

# PDF export with dimensions
pdf(file="plot.pdf", width=8, height=4)

# Setting up PDF output to show two plots side by side
par(mfrow=c(1,2))

# Plotting the data
plot(d$Year, mil(d$Bases), main = "Base Pairs by Year", xlab = "Year", ylab = "BP in Millions")
lines(d$Year, mil(d$Bases), type = "l", col = "Blue")
plot(d$Year, thou(d$Sequences), main = "Sequences by Year", xlab = "Year", ylab = "# Seq in Thousands")
lines(d$Year, thou(d$Sequences), type="l", col="Red")

# Turn off PDF output
dev.off()

