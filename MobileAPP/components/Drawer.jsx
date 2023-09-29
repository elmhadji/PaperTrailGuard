import { StyleSheet, } from 'react-native'
import { createDrawerNavigator  } from '@react-navigation/drawer'
import CustomeDrawerContent from './CustomeDrawerContent'
import CodeGenerator from './Pages/CodeGenerator'
import CodeReader from './Pages/CodeReader'


const Drawer = ({changeVisibility}) => {
  const Drawer = createDrawerNavigator()

  
    return (
      <Drawer.Navigator
        drawerContent={
              (props)=>
                <CustomeDrawerContent 
                  {...props} 
                  changeVisibility={changeVisibility}
                  />
            } 
        screenOptions={{
			headerStyle:{
				backgroundColor:'#2771FF',
			},
			headerTintColor:'#fff',
		}}
        >
        <Drawer.Screen 
			name="QR Code Reader" 
			component={CodeReader} 
            options={{unmountOnBlur:true}}
			/>
        <Drawer.Screen 
			name="QR Code Generator" 
			component={CodeGenerator} 
			/>
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
