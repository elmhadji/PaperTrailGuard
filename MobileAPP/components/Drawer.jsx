import { StyleSheet, Text, View } from 'react-native'
import { createDrawerNavigator  } from '@react-navigation/drawer'
import CustomeDrawerContent from './CustomeDrawerContent'
import HomeScreen from './HomeScreen'
import SettingsScreen from './SettingsScreen'

const Drawer = () => {
  const Drawer = createDrawerNavigator()
  
    return (
      <Drawer.Navigator
        drawerContent={(props)=><CustomeDrawerContent {...props}/>} >
        <Drawer.Screen name="Home" component={HomeScreen} />
        <Drawer.Screen name="Setting" component={SettingsScreen} />
      </Drawer.Navigator>
    )
};

export default Drawer;

const styles = StyleSheet.create({
  drawer: {
    backgroundColor: '#ffffff',
    borderWidth: 1,
    borderColor: '#000000',
  },
  header: {
    backgroundColor: '#0000ff',
    color: '#ffffff',
  },
});
