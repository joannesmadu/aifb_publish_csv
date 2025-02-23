# Create a PDF for the Renewable Energy Industry Report

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style="", size=12)

# Title
pdf.set_font("Arial", style="B", size=16)
pdf.cell(200, 10, "Renewable Energy Industry Report", ln=True, align="C")
pdf.ln(10)

# Table of Contents
pdf.set_font("Arial", style="B", size=14)
pdf.cell(200, 10, "Table of Contents", ln=True)
pdf.set_font("Arial", size=12)
contents = [
    "1. Introduction", "2. Market Trends", "   - Global Capacity Expansion",
    "   - Technological Advancements", "   - Policy and Investment Landscape",
    "3. Key Players", "   - Leading Companies", "   - Emerging Markets",
    "4. Challenges", "   - Economic and Political Factors", "   - Supply Chain and Infrastructure",
    "5. Future Projections", "   - Growth Forecasts", "   - Strategic Recommendations",
    "6. Conclusion", "7. References"
]
for item in contents:
    pdf.cell(0, 10, item, ln=True)

# Content Sections
sections = {
    "Introduction": "Renewable energy has become a pivotal component of the global energy landscape, "
                    "offering sustainable alternatives to fossil fuels. As of 2024, renewables account "
                    "for nearly 20% of global final energy consumption, up from 13% in 2023. This surge "
                    "is attributed to continuous policy support, declining costs, and the expanding use "
                    "of electricity in transport and heating sectors.",
    
    "Global Capacity Expansion": "In 2024, the world added over 5,500 gigawatts (GW) of renewable energy "
                                 "capacity. Solar photovoltaics (PV) led this growth, contributing approximately "
                                 "80% of the new capacity. The International Energy Agency (IEA) projects that "
                                 "renewables will meet almost half of the global electricity demand by 2030.",
    
    "Technological Advancements": "Technological innovation continues to drive the renewable sector. The cost "
                                   "of solar panels has significantly decreased, largely due to China's investments, "
                                   "making solar energy more accessible worldwide. Additionally, the integration of "
                                   "battery storage solutions is enhancing grid stability and reliability.",
    
    "Policy and Investment Landscape": "Global investments in clean energy are approaching the scale of fossil fuel "
                                        "investments. In 2024, China invested approximately $940 billion in clean "
                                        "energy. However, political shifts, such as changes in U.S. federal funding for "
                                        "clean energy projects, have introduced uncertainties in the investment climate.",
    
    "Key Players": "Major corporations like Ørsted have historically led the renewable energy market. However, recent "
                   "challenges, including rising costs and economic hurdles, have impacted their market positions. "
                   "Conversely, companies in China have expanded their influence, with significant contributions to "
                   "global renewable capacity growth.",
    
    "Challenges": "The industry faces several challenges, including economic and political factors, as well as supply "
                  "chain limitations. High interest rates and political decisions have introduced volatility in the "
                  "renewable energy sector, and supply chain disruptions continue to affect project timelines.",
    
    "Future Projections": "Despite challenges, the renewable energy sector is poised for continued growth. The IEA "
                          "indicates that while significant capacity additions are expected, current trajectories may "
                          "fall short of the United Nations' goal to triple renewable energy capacity by 2030. Achieving "
                          "this target will require enhanced policy measures, technological innovation, and substantial "
                          "investments.",
    
    "Strategic Recommendations": "To navigate the evolving landscape, stakeholders should consider policy advocacy, "
                                  "investment in technological innovation, and diversified supply chains to mitigate risks.",
    
    "Conclusion": "The renewable energy sector stands at a critical juncture, balancing opportunities for growth with "
                  "challenges arising from economic, political, and infrastructural factors. Success in this dynamic "
                  "environment will depend on strategic investments, policy support, and technological innovation.",
    
    "References": "1. International Energy Agency (2024) *Renewables 2024: Global Overview*. Available at: https://www.iea.org/reports/renewables-2024/global-overview\n"
                  "2. Reuters (2025) *China's clean energy investments nearing scale of global fossil investments*. Available at: https://www.reuters.com/world/china/chinas-clean-energy-investments\n"
                  "3. The Atlantic (2024) *Cheap Solar Panels Are Changing the World*. Available at: https://www.theatlantic.com/science/archive/2024/10/solar-power-energy-revolution\n"
                  "4. The Guardian (2025) *Solar has taken off in red states. Trump's funding freeze is causing panic*. Available at: https://www.theguardian.com/us-news/2025/feb/17/red-states-solar-trump-funding-freeze"
}

# Add sections to PDF
pdf.ln(5)
pdf.set_font("Arial", style="B", size=14)
for title, content in sections.items():
    pdf.cell(0, 10, title, ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    pdf.ln(5)

# Save PDF
pdf_filename = "/mnt/data/Renewable_Energy_Industry_Report.pdf"
pdf.output(pdf_filename)

# Provide download link
pdf_filename
