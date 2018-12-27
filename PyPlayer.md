# PyPlayer

## Modules

### I.Player

#### Functions:

##### 		Baslic

  1. Play music

     + 1.1 Event controlled

     + 1.2 Using specific signal to send event, switch pause state or stop state to play state
     + 1.3 If no music loaded, load 1st music from current play list and switch to play state, if can't load, disable this button

  2. Change current music

     + 2.1 Event controlled

     + 2.2 Using specific signal to send event and music information
     + 2.3 If get a wrong music(not exist or can't be loaded), jump to next music in play list

  3. Pause

     + 3.1 Event controlled

     + 3.2 Using specific signal to send event, switch playing state to pause state

  4. Continue

     + 4.1 Event controlled

     + 4.2 Using specific signal to send event, switch pause state or stop state to play state
     + 4.3 If no music loaded, stay in stop state and disable this button

  5. Volume increase

     + 6.1 Event controlled
     + 6.2 Using specific signal to send event and volume value

  6. Volume decrease

     + 7.1 Event controlled
     + 7.2 Using the same signal with Volume increase function

  7. Mute

     + 8.1 Event controlled
     + 8.2 Using the same signal with Volume increase function but send 0 volume
     + 8.3 Set mute icon

  8. Set play progress through the slider

     + 8.1 Event controlled
     + 8.2 Using a specific signal to send event and play progress
     + 8.3 If player in stop mode, disable progress bar

  9. Get play progress and time tick

     + 9.1 Event controlled
     + 9.2 Using timer to get playing time

##### Advance

   	1. Play style
   	2. Fast play
   	3. Play on Bluetooth device
   	4. Play MV
   	5. Show wave form of music like Windows XP Media Player method

#### UI

##### Basic

 1. Progress bar

 2. Volume set bar

##### Advance

   	1. All UI customized

#### Signals

 	1. Play signal
     + 1.1 Music reference
 	2. Pause signal
     + 2.1 None
 	3. Volume signal
     + 3.1 Volume value
 	4. Progress signal
     + 4.1 Time through start playing current music

----------------------

### II.Play list

#### Functions

##### Basic

1. Next music
2. Previous music
3. Sequential play
4. Random play
5. Single music loop
6. Add item(s)
7. Remove item(s)
8. Save on disk
9. Restore from disk
10. Initialize from music list

#### UI

##### Basic

1. Play mod setting pannel
2. Next button
3. Previous button
4. Display button
5. Show list
6. Remove from list button

##### Advance

1. All UI customize
2. Using icons instead of text

------------------------------

### III.Music list

#### Functions

##### Basic

 	1. Default list is LIKE
 	2. Add item(s)
 	3. Remove item(s)
 	4. Sort(Time, Singer, custom)
 	5. Search(Name, Singer, Regex)

#### UI

##### Basic

 	1. Display tree view
 	2. Add all to play list
 	3. Cover

##### Advance

 	1. All UI customize

----------

### IV. MusicItem

#### Functions

##### Basic

 	1. Add to music list
 	2. Add to play list
 	3. Like
 	4. Delete
 	5. Play next
 	6. Show information
 	7. Change information

##### Advance

 	1. Set lyric
 	2. Share(if online)
 	3. Download(if online)

