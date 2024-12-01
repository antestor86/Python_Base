def aplitude_score(start,end):
    count = 0
    attenuation = 0
    while start >  end:
        if start > end:
            attenuation = (start * 8.4 )/100
            start = start - attenuation
            count += 1
    return count

start_amplitide = float(input("Add Start Amplitude: "))
end_amplitude = float(input("Add End Amplitude: "))
result = aplitude_score(start_amplitide,end_amplitude)
print(result)