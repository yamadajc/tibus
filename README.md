![Portada](https://github.com/antoniogarciagiron/Project-Pandas-Shark-Attack/blob/main/images/tiburon.jpg)

# **Shark Attacks**

## 01. Introduction

- The target of the current project was to take a dataset, clean it and analyse the data. This is one of the projects done during the [IronHack](https://www.ironhack.com/es) Data Analytics bootcamp.
- The selected dataset was created by Toby Jolly and can be downloaded from [Kaggle](https://www.kaggle.com/teajay/global-shark-attacks). In this case the original dataset was a csv file with shark attacks information.
- The following Python libraries were used to sort the data and perform the analysis: Pandas, Re (Regex), Numpy and Seaborn.

## 02. Hypothesis

- My first hypothesis was that shark attacks depend on the time during the year, as most sharks are migratory animals. In particular, I wanted to know if shark attacks are produced during the warm months.
- My second task was to take as much usefull information as I can from the dataset.

## 03. Cleaning data

- The raw dataset had 25.000 rows and 24 columns, however, most rows didn't contain any information, and some columns were either empty or containing useless information.
- Some columns contain usefull information but the data was not well registered. I used Regex to find the usefull data and clean the rest.
- Also some column names were not correctly written, I changed the names to avoid confusion.
- The columns with repeated data were removed.
- After cleaning the null information and empty columns, the final dataset dimension was 6.293 x 13.

## 04. Results

After sorting the dataset, the most straightforward information to study was the relation between the age of the shark victims and the attacks, as shown as follows:

![Fig1](https://github.com/antoniogarciagiron/Project-Pandas-Shark-Attack/blob/main/images/01_victims.jpg)

In this figure it can be observed that most shark victims are males younger than 20 years. This is probably related with people practising water sports.
To confirm this hypothesis, the activities performed by the victims during the shark attacks were studied and plotted in the next graphic:

![Fig2](https://github.com/antoniogarciagiron/Project-Pandas-Shark-Attack/blob/main/images/02_Activities.jpg)

As espected, the two major activities were surfing and swimming, and among the 10 most recurrent activities only fishing is not related with a extreme sport.

The initial hypothesis is that sharks attack when the waters are warmer. The next plot shows the distribution of the shark attacks during the day:

![Fig3](https://github.com/antoniogarciagiron/Project-Pandas-Shark-Attack/blob/main/images/03_Daytime.jpg)

Most of the shark attacks happen during the afternoon, followed by the mornings, however this doesn't give any conclusion, as those are the times when people is usually practising sports. During the night people is sleeping.

The following figure shows the distribution of shark attacks by month: 

![Fig4](https://github.com/antoniogarciagiron/Project-Pandas-Shark-Attack/blob/main/images/04_Months.jpg)

It can be observed that there are two maximums in the shark attack tendence, in July and January, to understand this fact it is necesary to separate the data by hemispheres.
The countries with more shark attacks registered are USA, Australia and South Africa, in that order, being the first one in the Northern Hemisphere and the other two in the Southern Hemisphere. Splitting the data by country we can observe the following results:

![Fig5](https://github.com/antoniogarciagiron/Project-Pandas-Shark-Attack/blob/main/images/05_Months_vs_country.jpg)

It is clear that shark attacks are following a pattern. In USA the attacks are concentrated in the warm months, and the same happens in Australia and South Africa. Water extreme sports and fishing are not only practised during the summer, and the tendence could be linked with the migratory tendences of some sharks, as the great White shark.

Another interesting fact to study is if the sharks are more agresive during certain hours in the day. The following graph shows the ratio sirvival/fatal attack splitted by daytimes:

![Fig6](https://github.com/antoniogarciagiron/Project-Pandas-Shark-Attack/blob/main/images/06_Daytime_vs_Fatal.jpg)

There is not a link between the fatal attacks and the day time, however, the ratio during the night is higher, so don't practise surf during the night...

Follwing the study on the fatal attacks and the survival ratio, it is interesting to study the most deadly species. The next graph shows the survival and fatal attacks splitted by shark species:

![Fig7](https://github.com/antoniogarciagiron/Project-Pandas-Shark-Attack/blob/main/images/08_Fatal_shark_attacks.jpg)

There most active shark is the great White shark, as expected from the king of the oceans, and the Tiger and Bull sharks are the ones following the list. Almost all the fatal attacks are carried out by White, Tiger and Bull sharks (There are also registers of Blue and Zambesi shark fatal attacks). The rest of the shark species are also attacking humans, but the survival ratio is almost a 100%. Even though a shark attack is one of the worst sailor's nightmare, there is almost a 75% chance to survive to a White, Tiger or Bull shark. There is always hope...

Furthermore, it is important to identify the most dangerous areas in terms of shark attacks. The following figure shows the countries with more shark attacks and the species:

![Fig8](https://github.com/antoniogarciagiron/Project-Pandas-Shark-Attack/blob/main/images/09_Species_vs_country.jpg)

A deeper study would be necessary to bring conclusions, but at first glance, the countries  as Australia, USA and South Africa, with an extended surfer culture, suffer more attacks.

The survival ratio by age is almost constant, however, it is reduced for ages below 10 and above 60, as shown here:

![Fig9](https://github.com/antoniogarciagiron/Project-Pandas-Shark-Attack/blob/main/images/10_Survival_Age.jpg)

When you have to fight with a shark is better if you are fast and strong...

The last figure to show plots the number of registered attacks per year:

![Fig10](https://github.com/antoniogarciagiron/Project-Pandas-Shark-Attack/blob/main/images/07_Attacks_year.jpg)

There is an ascending trend, probably produced by the higher number of people practising water sports, combined with the better techologies to store and track data.
Fun fact: it can be observed a local minimum around the year 1975, suggesting a reduction in the shark attacks. The movie Jaws was released in 1975, maybe people was so scared of sharks that decided to practise mountain sports...

## 05. Conclusions

A dataset containing information about shark attacks was cleaned and analysed, showing some interesting information, as the distribution of attacks during the warm months or the favourite shark victims, i.e. young males practising water extreme sports. 