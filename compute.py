def visualize_series(
    Q1, # string, title
    Q2,
    Q3,Q4,Q5,Q6,
    Q3b,Q4b,Q5b,Q6b,
    Q3c,Q4c,Q5c,Q6c,
    Q7,Q8,Q11 # values from questions, 1 2 3 or 4
    ):
    # Turn independent variable into sympy symbol, stored in x
    import matplotlib.pyplot as plt
    import numpy as np


    labels = ['CLR', 'PNLRA', 'NRWRA']

    Q2to10=[Q2,Q3,Q4,Q5,Q6,Q3b,Q4b,Q5b,Q6b,Q3c,Q4c,Q5c,Q6c,Q7,Q8,Q11]
    # Translate to factor values
    Tot =  Q2to10.count(1) + Q2to10.count(2) + Q2to10.count(3)
    FA = Q2to10.count(1)/Tot #1-A: Control factor
    FB = Q2to10.count(2)/Tot #2-B: Subjective factor
    FC = Q2to10.count(3)/Tot #3-C: Social factor
    values = [FA,FB,FC]

    # Calculate total score as result area / maximum area
    # Goes grom [0-1], 0 is for 'pure' factor, 1 to perfectly equilibrated experiment
    area = (FA*FB*np.sin(120))/2 + (FB*FC*np.sin(120))/2 +(FA*FC*np.sin(120))/2
    PerEquilArea = ((((Tot/3)/Tot)*((Tot/3)/Tot)*np.sin(120))/2)*3 # Maximun posible area (all load the same weight)

    TotScore = area/PerEquilArea

    textstr =     'CLR = ' + str(round(values[0]*100,1)) + \
              '% | PNLRA = ' + str(round(values[1]*100,1) )+ \
              '% | NRWRA = ' + str(round(values[2]*100,1)) + \
              '% | BE = ' + str(round(TotScore,2))

    
    legenda = '\n'.join((
    r'CLR = Controlled laboratory research | PNLRA = Partially naturalistic laboratory research approach',
    r' NRWRA = Naturalistic real-world research approach | BE = Balance Score'))
    # legenda = '\n'.join((
    # r'CLR = Controlled laboratory research | PNLRA = Partially naturalistic laboratory research approach',
    # r' NRWRA = Naturalistic real-world research approach'))

    num_vars = len(labels)
    # Split the circle into even parts and save the angles
    # so we know where to put each axis.
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # The plot is a circle, so we need to "complete the loop"
    # and append the start value to the end.
    values += values[:1]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    # Draw the outline of our data.
    ax.plot(angles, values, color='#fe630f', linewidth=1)
    # Fill it in.
    ax.fill(angles, values, color='#e08162', alpha=0.25)
    
    # Fix axis to go in the right order and start at 12 o'clock.
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    
    # Draw axis lines for each angle and label.
    ax.set_thetagrids(np.degrees(angles), labels)
    
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
    ax.set_title(Q1, y=1.08)
    # place a text box in upper left in axes coords
    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='#e08162', alpha=0.25)
    ax.text(-0.05, -0.02, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top')
    ax.text(-0.1, -0.07, legenda,transform=ax.transAxes, fontsize=8,
        verticalalignment='top')

    from io import BytesIO
    figfile = BytesIO()
    fig.savefig(figfile, format='png')
    figfile.seek(0)  # rewind to beginning of file
    import base64
    figdata_png = base64.b64encode(figfile.getvalue())
    return figdata_png.decode('utf8')

if __name__ == '__main__':
    visualize_series(Q1="Your study aim", Q2=1, 
    Q3=1, Q4=1, Q5=1, Q6=4,
    Q3b=2, Q4b=2, Q5b=2, Q6b=2,
    Q3c=3, Q4c=3, Q5c=3, Q6c=3,
    Q7=4, Q8=4, Q11=4)

