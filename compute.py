def visualize_series(numExp,intervention,
    Q1a,Q1b,# Text titles
    Q2,Q3,Q4,Q5,Q6,
    Q3b,Q4b,Q5b,Q6b,
    Q3c, Q4c,Q5c,Q6c,
    Q7,
    Q8 # values from questions, 1 2 3 or 4
    ):
# Code adapted from https://www.pythoncharts.com/matplotlib/radar-charts/
    import matplotlib.pyplot as plt
    import numpy as np

    labels = ['CLR', 'PNLRA', 'NRWRA']
    if intervention == 'No':
        if numExp == 1:
          Qtot=[Q2,Q3,Q4,Q5,Q6,Q7]
          evalRes = ['Q2,Sa','Q3,TS','Q4,Ta', 'Q5,St','Q6,M','Q7,Sk']


        elif numExp == 2:
          Qtot=[Q2,Q3,Q4,Q5,Q6,Q3b,Q4b,Q5b,Q6b,Q7]
          evalRes = ['Q2,Sa.','Q3,TS','Q4,Ta', 'Q5,St','Q6,Me',
                     'Q2.2,Sa','Q3.2,TS','Q4.2,Ta', 'Q5.2,St','Q6.2,M',
                     'Q7,Sk']
        else:
          Qtot=[Q2,Q3,Q4,Q5,Q6,Q3b,Q4b,Q5b,Q6b,Q3c,Q4c,Q5c,Q6c,Q7]
          evalRes = ['Q2,Sa','Q3,TS','Q4,Ta', 'Q5,St','Q6,M',
                     'Q2.2,Sa','Q3.2,TS','Q4.2,Ta', 'Q5.2,St','Q6.2,M',
                     'Q2.3,Sa','Q3.3,TS','Q4.3,Ta', 'Q5.3,St','Q6.3,M',
                     'Q7,Sk']

    else:
        if numExp == 1:
          Qtot=[Q2,Q3,Q4,Q5,Q6,Q7,Q8]
          evalRes = ['Q2,Sa','Q3,TS','Q4,Ta', 'Q5,St','Q6,M',
                     'Q7,Sk','Q8.I' ]

        elif numExp == 2:
          Qtot=[Q2,Q3,Q4,Q5,Q6,Q3b,Q4b,Q5b,Q6b,Q7,Q8]
          evalRes = ['Q2,Sa','Q3,TS','Q4,Ta', 'Q5,St','Q6,M',
                    'Q2.2,Sa','Q3.2,TS','Q4.2,Ta', 'Q5.2,St','Q6.2,M',
                     'Q7,Sk','Q8.I']

        else:
          Qtot=[Q2,Q3,Q4,Q5,Q6,Q3b,Q4b,Q5b,Q6b,Q3c,Q4c,Q5c,Q6c,Q7,Q8]
          evalRes = ['Q2,Sa','Q3,TS','Q4,Ta', 'Q5,St','Q6,M',
                    'Q2.2,Sa','Q3.2,TS','Q4.2,Ta', 'Q5.2,St','Q6.2,M',
                    'Q2.3,Sa','Q3.3,TS','Q4.3,Ta', 'Q5.3,St','Q6.3,M',
                     'Q7,Sk','Q8.I']
    
    FA_val = [val for is_FA, val in zip([x == 1 for x in Qtot ], evalRes) if is_FA]
    FB_val = [val for is_FB, val in zip([x == 2 for x in Qtot ], evalRes) if is_FB]
    FC_val = [val for is_FB, val in zip([x == 3 for x in Qtot ], evalRes) if is_FB]


    # Translate to factor values
    Tot =  Qtot.count(1) + Qtot.count(2) + Qtot.count(3)
    FA = Qtot.count(1)/Tot #1-A: Control factor
    FB = Qtot.count(2)/Tot #2-B: Subjective factor
    FC = Qtot.count(3)/Tot #3-C: Social factor
    values = [FA,FB,FC]

    # Calculate total score as result area / maximum area
    # Goes grom [0-1], 0 is for 'pure' factor, 1 to perfectly equilibrated experiment
    area = (FA*FB*np.sin(120))/2 + (FB*FC*np.sin(120))/2 +(FA*FC*np.sin(120))/2
    PerEquilArea = ((((Tot/3)/Tot)*((Tot/3)/Tot)*np.sin(120))/2)*3 # Maximun posible area (all load the same weight)

    TotScore = area/PerEquilArea

    textstr =     'CLR = ' + str(round(values[0]*100,1)) + \
              '% | PNLRA = ' + str(round(values[1]*100,1) )+ \
              '% | NRWRA = ' + str(round(values[2]*100,1)) + \
              '% | BS = ' + str(round(TotScore,2))

    
    legenda = '\n'.join((
    r'CLR: '+'; '.join(FA_val),
    r'PNLRA: ' +'; '.join(FB_val) ,
    r'NRWRA: ' +'; '.join(FC_val)))
    #legenda = '\n'.join((
    #r'CLR = Controlled laboratory research | PNLRA = Partially naturalistic laboratory research approach',
    #r' NRWRA = Naturalistic real-world research approach | BS = Balance Score'))

    num_vars = len(labels)
    # Split the circle into even parts and save the angles
    # so we know where to put each axis.
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # The plot is a circle, so we need to "complete the loop"
    # and append the start value to the end.
    values += values[:1]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(7,7), subplot_kw=dict(polar=True))
    fig.suptitle('Behavior:' + Q1a, fontsize=14, fontweight='bold', color='#4A4A4A')

    # Draw the outline of our data.
    ax.plot(angles, values, color='#fe630f', linewidth=1)
    # Fill it in.
    ax.fill(angles, values, color='#e08162', alpha=0.25)
    
    # Fix axis to go in the right order and start at 12 o'clock.
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    
    # Draw axis lines for each angle and label.
    ax.set_thetagrids(np.degrees(angles),  ['CLR', 'PNLRA', 'NRWRA','CLR'])
    
    # Go through labels and adjust alignment based on where
    # it is in the circle.
    for label, angle in zip(ax.get_xticklabels(), angles):
      if angle in (0, np.pi):
        label.set_horizontalalignment('center')
      elif 0 < angle < np.pi:
        label.set_horizontalalignment('left')
      else:
        label.set_horizontalalignment('right')
       
    # Set position of y-labels to be in the middle
    # of the first two axes.
    ax.set_rlabel_position(180 / num_vars)
    
    # Add some custom styling.
    # Change the color of the tick labels.
    ax.tick_params(colors='#222222')
    # Make the y-axis (0-100) labels smaller.
    ax.tick_params(axis='y', labelsize=8)
    # Change the color of the circular gridlines.
    ax.grid(color='#AAAAAA')
    # Change the color of the outermost gridline (the spine).
    ax.spines['polar'].set_color('#222222')
    # Change the background color inside the circle itself.
    ax.set_facecolor('#FAFAFA')
    
    # Add chart a title and summary.
    fig.subplots_adjust(top=0.85)
    ax.set_title('Context: ' + Q1b, y=1.08,color = '#6B6B6B')

    # place a text box in upper left in axes coords
    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='#e08162', alpha=0.25)
    ax.text(0.5, -0.02, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', horizontalalignment='center')
    ax.text(0.5, -0.07, legenda,transform=ax.transAxes, fontsize=8,
        verticalalignment='top', horizontalalignment='center')

    from io import BytesIO
    figfile = BytesIO()
    fig.savefig(figfile, format='png')
    figfile.seek(0)  # rewind to beginning of file
    import base64
    figdata_png = base64.b64encode(figfile.getvalue())
    return figdata_png.decode('utf8')

if __name__ == '__main__':
    visualize_series(numExp = 3,intervention = 'Yes',
      Q1a="Your study aim",Q1b="Context",# Text titles
      Q2=1, # Sample
      Q3=1, # Testing site
      Q4=1, # Task
      Q5=1, # Stimuli
      Q6=1, # Measures
      Q3b=2,
      Q4b=2,
      Q5b=3,
      Q6b=2,
      Q3c=4,
      Q4c=3,
      Q5c=4,
      Q6c=4,
      Q7=1, # Stakeholders
      # Interventon questions 
      Q8=1)
