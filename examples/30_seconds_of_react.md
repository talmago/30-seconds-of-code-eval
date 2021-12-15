#### useUnload (task/1)

```diff
-const useUnload = fn => {
+const useUnload = fn => {
+
+    for ( let i = 0 ; i < R . length ; i ++ ) {
+    if ( R [i] === fn) {
+    R . splice (i, 1 );
+    break ;
+    }
```

#### useUnload (task/1)

```diff
-const useUnload = fn => {
+const useUnload = fn => {
+
+    const unload = [ ' backgroundImage ' , ' backgroundSize ' , ' borderImageOutset ' , ' borderImageWidth ' , ' borderRadius ' , ' boxShadow ' , ' clip ' , ' direction ' , '
```

#### useUnload (task/1)

```diff
-const useUnload = fn => {
+const useUnload = fn => {
+ const unloadFunction = () => { if ( typeof fn === 'function' ) { fn () } else { if ( a . event . add ) { a . event . add ( a . el , 'unload' , unload
```

#### useUnload (task/1)

```diff
-const useUnload = fn => {
+const useUnload = fn => {
+ let previousReturnedObject; return function () { if (previousReturnedObject === undefined) { previousReturnedObject = this; } previousReturnedObject = undefined; fn.apply(this, arguments); }; }; const useReturn =
```

#### useUnload (task/1)

```diff
-const useUnload = fn => {
+const useUnload = fn => {
+ let { node, isImmediate } = useWithNode(fn); return node.useUnload() || isImmediate ? Unload(node) : fn(...arguments); };
+    This technique is also useful for code that
```

#### useClickOutside (task/2)

```diff
-const useClickOutside = (ref, callback) => {
+const useClickOutside = (ref, callback) => {
+ ref.use(callback) .click(callback) .click(callback) .click(callback) .click(callback) .click(callback) .click(callback) .click(callback) .click(callback) .click(callback
```

#### useClickOutside (task/2)

```diff
-const useClickOutside = (ref, callback) => {
+const useClickOutside = (ref, callback) => {
+
+    let _ref = ref;
+    function _callback () {
+    callback.call(_ref);
+    _ref = null;
+    }
+    ref.addEventListener('click', _callback);
+    };
```

#### useClickOutside (task/2)

```diff
-const useClickOutside = (ref, callback) => {
+const useClickOutside = (ref, callback) => {
+
+    const el = document.querySelector('.grid-col-axis-page');
+    const col = el.querySelector('.grid-col-axis-page-column');
+    const parent = col.parent
```

#### useClickOutside (task/2)

```diff
-const useClickOutside = (ref, callback) => {
+const useClickOutside = (ref, callback) => {
+
+    let start = Date.now();
+    ref.on("click", () => {
+    let stop = Date.now();
+    callback && callback();
+    callback = null;
+    let diff = stop - start;
```

#### useClickOutside (task/2)

```diff
-const useClickOutside = (ref, callback) => {
+const useClickOutside = (ref, callback) => {
+
+    let previousButton = ref.querySelector('.material-ui-button-primary-outer');
+    if (previousButton.closest('[class*="js-use-click-outside"]').length >
```

#### useSessionStorage (task/3)

```diff
-const useSessionStorage = (keyName, defaultValue) => {
+const useSessionStorage = (keyName, defaultValue) => {
+
+    return new Promise((resolve, reject) => {
+    const sessionStorage = window.sessionStorage ||
+    window.localStorage;
+    if (sessionStorage.setItem) {
+    sessionStorage.setItem(
```

#### useSessionStorage (task/3)

```diff
-const useSessionStorage = (keyName, defaultValue) => {
+const useSessionStorage = (keyName, defaultValue) => {
+
+    return new Promise((resolve, reject) => {
+    sessionStorage.setItem(keyName, value)
+    .then(() => {
+    if (value !== null) {
+    resolve(value
```

#### useSessionStorage (task/3)

```diff
-const useSessionStorage = (keyName, defaultValue) => {
+const useSessionStorage = (keyName, defaultValue) => {
+ let _key = keyName; if (typeof localStorage[_key] === 'undefined') { localStorage[_key] = defaultValue; } return localStorage[_key]; }; const getItem = keyName => {
```

#### useSessionStorage (task/3)

```diff
-const useSessionStorage = (keyName, defaultValue) => {
+const useSessionStorage = (keyName, defaultValue) => {
+
+    const storage = localStorage.getItem(keyName);
+    if (!storage) {
+    return defaultValue;
+    }
+    return JSON.parse(storage);
+    };
+    const logSessionStorage = (
```

#### useSessionStorage (task/3)

```diff
-const useSessionStorage = (keyName, defaultValue) => {
+const useSessionStorage = (keyName, defaultValue) => {
+
+    const key = new Map()
+    return sessionStorage.getItem(keyName) || (key.set(keyName, defaultValue) && key.get(keyName))
+    }
+    const isServer = ()
```

#### useTitle (task/4)

```diff
-const useTitle = title => {
+const useTitle = title => {
+
+    const s = document.querySelector('h1').textContent;
+    return title === s ? '<h1>' + title + '</h1>' : null;
+    };
+    const useH
```

#### useTitle (task/4)

```diff
-const useTitle = title => {
+const useTitle = title => {
+
+    const {
+    site,
+    } = makeApiUrl (title)
+    const titleAndSite = ` ${ site . title } / ${ title } `
+    return titleAndSite
+    }
+    const use
```

#### useTitle (task/4)

```diff
-const useTitle = title => {
+const useTitle = title => {
+
+    const txt = useState(title);
+    const { isFirst } = useState(false);
+    const { count } = useState(0);
+    const {
+    next,
+    done,
```

#### useTitle (task/4)

```diff
-const useTitle = title => {
+const useTitle = title => {
+ if (title) { return < h1 className = {styles.header} > {title} < / h1 > ; } else { return < h1 className = {styles.header} > Loading < / h1 > ;
```

#### useTitle (task/4)

```diff
-const useTitle = title => {
+const useTitle = title => {
+
+    const input = dom.get(`input.title`);
+    const placeholder = dom.get(`input.placeholder`);
+    input.value = title;
+    input.setAttribute('placeholder', placeholder
```

#### useEffectOnce (task/5)

```diff
-const useEffectOnce = (callback, when) => {
+const useEffectOnce = (callback, when) => {
+ let once = false; return () => { if (once) { return; } once = true; callback(); when(); }; }; function addOne() { console.log(1); } const useEffectOncePromise = () => { let
```

#### useEffectOnce (task/5)

```diff
-const useEffectOnce = (callback, when) => {
+const useEffectOnce = (callback, when) => {
+
+    const memoizedCallback = memoize(callback);
+    const handleCalls = (previousState, ...nextArgs) => {
+    if (typeof previousState === 'function') {
+    const call = previousState
```

#### useEffectOnce (task/5)

```diff
-const useEffectOnce = (callback, when) => {
+const useEffectOnce = (callback, when) => {
+ const action = () => { callback(); }; return () => { if (when.fire()) { action(); } }; }; const oneTimeUse = useEffectOnce(() => { console.log('once') }, 0); oneTimeUse();
```

#### useEffectOnce (task/5)

```diff
-const useEffectOnce = (callback, when) => {
+const useEffectOnce = (callback, when) => {
+
+    let id;
+    if (when) {
+    id = setInterval(() => {
+    callback();
+    }, 1000);
+    } else {
+    callback();
+    }
+    return () => {
```

#### useEffectOnce (task/5)

```diff
-const useEffectOnce = (callback, when) => {
+const useEffectOnce = (callback, when) => {
+
+    const effect = useEffect(() => {
+    callback();
+    }, when);
+    effect.then(() => {
+    effect = null;
+    });
+    return effect;
+    };
+    //
```

#### Accordion (task/6)

```diff
-const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+ const { onClick } = this.props; return ( <div className="accordion-item"> <div className="accordion-title"> { label } </div> <div className="accordion-
```

#### Accordion (task/6)

```diff
-const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+ const content = isCollapsed ? "" : children return ( <div className="accordion-item"> <div className="accordion-item-heading"> <h3 className="accordion-heading">{label
```

#### Accordion (task/6)

```diff
-const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+ const propTypes = { isCollapsed: PropTypes.bool.isRequired, label: PropTypes.string.isRequired, handleClick: PropTypes.func.isRequired, children: PropTypes.any.isRequired }; return (
```

#### Accordion (task/6)

```diff
-const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+ return ( <li> <div className="panel panel-default"> <div className="panel-heading"> <h3 className="panel-title">{label}</h3> </div> <div className="panel
```

#### Accordion (task/6)

```diff
-const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+
+    const className = isCollapsed ? "expanded" : "collapsed";
+    return (
+    <div className={className} onClick={() => handleClick(label)}>
+    {children}
```

#### useIsomporphicEffect (task/7)

```diff
-const useIsomorphicEffect =
+const useIsomorphicEffect =
+ require ( ' use-isomorphic-effect ' ) ;
+    useEffect
+    useEffect is mostly the same as useEffect , except it adds a cleanup function to the effect if the value is not needed anymore.
+    Example:
```

#### useIsomporphicEffect (task/7)

```diff
-const useIsomorphicEffect =
+const useIsomorphicEffect =
+ () => {
+    const register = (store) => {
+    if (store.isomorphic) {
+    const {
+    ...customData,
+    ...defaultData
+    } = useEffect(() => {
```

#### useIsomporphicEffect (task/7)

```diff
-const useIsomorphicEffect =
+const useIsomorphicEffect =
+ require ( ' use-isomorphic-effect ' ) ;
+    import { log } from ' ./util ' ;
+    import { bindActionCreators } from ' ./reducers ' ;
+    import { connect } from ' react
```

#### useIsomporphicEffect (task/7)

```diff
-const useIsomorphicEffect =
+const useIsomorphicEffect =
+ require ( ' use-isomorphic-effect ' )
+    const isomorphicEffect = useIsomorphicEffect (isomorphicEffect)
+    // import { createStore } from 'redux'
+    // const store = createStore(root
```

#### useIsomporphicEffect (task/7)

```diff
-const useIsomorphicEffect =
+const useIsomorphicEffect =
+ (() => import( ' isomorphic-fetch ' ));
+    export const mockAxios = () => {
+    return {
+    get: jest.fn(),
+    };
+    };
+    const initialState = {
```

#### useGetSet (task/8)

```diff
-const useGetSet = initialState => {
+const useGetSet = initialState => {
+
+    const [state, setState] = useState(initialState);
+    return {
+    set(state, value) {
+    setState(state, value);
+    },
+    get() {
+    return state
```

#### useGetSet (task/8)

```diff
-const useGetSet = initialState => {
+const useGetSet = initialState => {
+
+    const [ value , setValue ] = useState ( initialState );
+    return {
+    get : () => value ,
+    set : ( newValue ) => setValue ( newValue )
+    };
+    };
```

#### useGetSet (task/8)

```diff
-const useGetSet = initialState => {
+const useGetSet = initialState => {
+ const { set, get } = call(store, initialState); return { ...initialState, [get] : get, [set] : set }; };
+    And now we have one less action to build!
+    // In the
```

#### useGetSet (task/8)

```diff
-const useGetSet = initialState => {
+const useGetSet = initialState => {
+ return { ...initialState, [actionName] : initialState[actionName] } } const action = useReducer(useGetSet, initialState)
+    Keep in mind that this is a solution for the simplest use case, but
```

#### useGetSet (task/8)

```diff
-const useGetSet = initialState => {
+const useGetSet = initialState => {
+
+    const { value } = initialState;
+    return {
+    [ Symbol . iterator ] : function * ( ) {
+    let { done , value } = useState ( false ) ;
+    let next = value;
```

#### useInterval (task/9)

```diff
-const useInterval = (callback, delay) => {
+const useInterval = (callback, delay) => {
+
+    let interval = setInterval(() => {
+    callback();
+    if (delay === 1000) {
+    clearInterval(interval);
+    }
+    }, delay);
+    };
+    Here’
```

#### useInterval (task/9)

```diff
-const useInterval = (callback, delay) => {
+const useInterval = (callback, delay) => {
+
+    const id = setInterval(() => {
+    callback();
+    }, delay);
+    return id;
+    };
+    // ...
+    function *startSearch(query) {
+    const [currentPage,
```

#### useInterval (task/9)

```diff
-const useInterval = (callback, delay) => {
+const useInterval = (callback, delay) => {
+
+    let i = setInterval(() => {
+    callback();
+    if (delay > 0) {
+    let time = new Date().getTime() - i;
+    i = setInterval(() => {
```

#### useInterval (task/9)

```diff
-const useInterval = (callback, delay) => {
+const useInterval = (callback, delay) => {
+
+    if (delay <= 0) {
+    return setInterval(callback, 0);
+    }
+    return new Promise(resolve => {
+    clearInterval(intervalId);
+    callback();
+    res
```

#### useInterval (task/9)

```diff
-const useInterval = (callback, delay) => {
+const useInterval = (callback, delay) => {
+
+    let timer = setInterval(() => {
+    callback();
+    }, delay);
+    if (timer) {
+    callback();
+    }
+    };
+    // Simulate an expensive operation
+    useInter
```

#### Loader (task/10)

```diff
-const Loader = ({ size }) => {
+const Loader = ({ size }) => {
+
+    if (size) {
+    return <Loader size={size} />;
+    } else {
+    return <Loader />;
+    }
+    };
+    const Loader = ({ loader }) => {
+    return
```

#### Loader (task/10)

```diff
-const Loader = ({ size }) => {
+const Loader = ({ size }) => {
+
+    const { width, height } = size;
+    const options = {
+    canvas: {
+    width,
+    height,
+    },
+    };
+    return class extends React.Component {
+    constructor
```

#### Loader (task/10)

```diff
-const Loader = ({ size }) => {
+const Loader = ({ size }) => {
+ const el = DOM.div( {class: 'loader'}, Loader.step() ); return el; }; return Loader; };
+    To use this component:
+    <Loader />
+    We could use it with a component
```

#### Loader (task/10)

```diff
-const Loader = ({ size }) => {
+const Loader = ({ size }) => {
+ const loader = createLoader (size); return { get : () => { return loader . load (); }, }; };
+    Now we're ready to write our component's getInitialState and componentWillMount :
+    class App extends Component { state
```

#### Loader (task/10)

```diff
-const Loader = ({ size }) => {
+const Loader = ({ size }) => {
+
+    const { height, width } = size
+    return (
+    <div>
+    <img src={require('../assets/img/s.png')} />
+    <p>some text</p>
```

#### Modal (task/11)

```diff
-const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+ const show = () => { isVisible = true title = `Your mind is open` content = `This is what is needed to fix your problem.` footer = `The answer is in the reflection.` } const hide = ()
```

#### Modal (task/11)

```diff
-const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+ const closeHandler = () => { isVisible = false; } return ( <div className="modal"> <div className="modal-content"> <div className="modal-header"> <button type="button"
```

#### Modal (task/11)

```diff
-const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+ const overlay = () => { const modal = document.createElement('div'); modal.classList.add('modal-box'); modal.classList.add('modal-overlay'); return modal; }; return
```

#### Modal (task/11)

```diff
-const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+ const showDialog = () => { isVisible = true; }; const hideDialog = () => { isVisible = false; }; const closeDialog = () => { onClose() }; return ( <> <header> <h1>
```

#### Modal (task/11)

```diff
-const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+ const open = () => { isVisible = true; }; const close = () => { isVisible = false; }; return ( <div className="modal"> <div className="modal-header"> <button onClick
```

#### useIntersectionObserver (task/12)

```diff
-const useIntersectionObserver = (ref, options) => {
+const useIntersectionObserver = (ref, options) => {
+ return useRef(() => { const [prevValue, observer, oldValue] = useState([0]); const nextValue = ref.current.get(); if (nextValue === oldValue) { return; } const diff = nextValue
```

#### useIntersectionObserver (task/12)

```diff
-const useIntersectionObserver = (ref, options) => {
+const useIntersectionObserver = (ref, options) => {
+
+    const observer = new IntersectionObserver(
+    (entries) => {
+    const [, _ref] = entries;
+    if (!_ref) {
+    return;
+    }
+    const [,
```

#### useIntersectionObserver (task/12)

```diff
-const useIntersectionObserver = (ref, options) => {
+const useIntersectionObserver = (ref, options) => {
+
+    const target = ref.target;
+    const observer = new IntersectionObserver(
+    (entries, observer) => {
+    if (entries.length === 0) {
+    return;
+    }
```

#### useIntersectionObserver (task/12)

```diff
-const useIntersectionObserver = (ref, options) => {
+const useIntersectionObserver = (ref, options) => {
+
+    const observer = new IntersectionObserver(
+    (entries) => {
+    const [, target] = entries;
+    // Do stuff with the target element
+    }
+    );
+    observer.ob
```

#### useIntersectionObserver (task/12)

```diff
-const useIntersectionObserver = (ref, options) => {
+const useIntersectionObserver = (ref, options) => {
+ let observer = new IntersectionObserver(intersectionHandler, options); let parent = ref.parent; while (parent && !parent.disconnect) { parent = parent.parent; } return !!observer; }; const onScroll =
```

#### Slider (task/13)

```diff
-const Slider = ({ 
+const Slider = ({ 
+	value, 	min, 	max, 	step, 	orientation, 	... 	children }) => (
+    const min = value < min ? value : min;
+    const max = value > max
```

#### Slider (task/13)

```diff
-const Slider = ({ 
+const Slider = ({ 
+ids }) => ( <div> <SliderGroup size={[ids.length, 4]}> { [ids.map((id, i) => ( <Slider key={id} value={id} onChange={(id)
```

#### Slider (task/13)

```diff
-const Slider = ({ 
+const Slider = ({ 
+xtype }) => {
+    const Slider = ({ xtype }) => {
+    const slider = createElement ( xtype , {
+    const slider = createElement ( xtype , {
+    value : 0 ,
```

#### Slider (task/13)

```diff
-const Slider = ({ 
+const Slider = ({ 
+xtype, start, change, end, min, max, value, xtype, start, change, end, min, max, value, ... }, ...) => ( < React.Fragment > < React.Fragment > <
```

#### Slider (task/13)

```diff
-const Slider = ({ 
+const Slider = ({ 
+xtype, min, max, value, step, dir, floating, show, animate, duration, callback, extraParams, ease, onStart, onChange, onEnd, onTick }) => {
+    const _this =
```

#### useToggler (task/14)

```diff
-const useToggler = initialState => {
+const useToggler = initialState => {
+ const { toggleOpen, toggleClose } = state.use; return { ...initialState, toggleOpen, toggleClose }; }; const toggleState = useToggler(undefined); useToggler(toggleState); // 📄
```

#### useToggler (task/14)

```diff
-const useToggler = initialState => {
+const useToggler = initialState => {
+
+    let toggler = useToggler(initialState)
+    if (toggler) {
+    const [isOpen, setIsOpen] = useState(false)
+    const [closing, setCl
```

#### useToggler (task/14)

```diff
-const useToggler = initialState => {
+const useToggler = initialState => {
+
+    const { isOpen, toggle, ...state } = state;
+    const { isOpen, toggle, ...restState } = restState;
+    return { ...state, ...restState, isOpen, toggle };
```

#### useToggler (task/14)

```diff
-const useToggler = initialState => {
+const useToggler = initialState => {
+
+    const [ show , setShow ] = useState ( false );
+    const [ hide , setHide ] = useState ( true );
+    return {
+    show,
+    hide,
+    setShow,
+    set
```

#### useToggler (task/14)

```diff
-const useToggler = initialState => {
+const useToggler = initialState => {
+
+    const [ toggled , setToggled ] = useState ( false );
+    return {
+    ... initialState ,
+    [ toggled ]: useState ( initialState [ toggled ]),
```

#### useHover (task/15)

```diff
-const useHover = () => {
+const useHover = () => {
+ return { onMouseEnter: useHover, onMouseLeave: () => { useHover() }, }; } export default useHover;
+    And finally, in my main.js file, I imported all the components and told React
```

#### useHover (task/15)

```diff
-const useHover = () => {
+const useHover = () => {
+ const doc = document . querySelector ( '.text-editor' ); if ( doc . querySelector ( '.has-focus' )) { let focusStyle = doc . querySelector ( '.has-focus' ). style ; focusStyle
```

#### useHover (task/15)

```diff
-const useHover = () => {
+const useHover = () => {
+
+    const hover = document.querySelector('[use-hover]');
+    if (hover) {
+    hover.removeAttribute('use-hover');
+    }
+    };
+    const onError = (error)
```

#### useHover (task/15)

```diff
-const useHover = () => {
+const useHover = () => {
+ // this is my "event handler" (it's a function) if (this.classList.contains('hoverable')) { // this is my "event callback" (it's a function) this.classList.remove('
```

#### useHover (task/15)

```diff
-const useHover = () => {
+const useHover = () => {
+ document.getElementById('usehover').addEventListener('click', () => { document.getElementById('usehover').removeAttribute('disabled'); }) } const useBackground = () => { document.getElementById('usebackground').
```

#### usePrevious (task/16)

```diff
-const usePrevious = value => {
+const usePrevious = value => {
+ return { ...value, usePrevious }; }; return { ...user, [ ' usePrevious ' ] = usePrevious }; }; }
+    The following snippet shows a computed property that depends on the presence of another computed property ( foo ):
+    class
```

#### usePrevious (task/16)

```diff
-const usePrevious = value => {
+const usePrevious = value => {
+ return (previous < value) ? previous : value; }, output = usePrevious(0); // first usePrevious(1); // second usePrevious(2); // third
+    As you can see, the outputs don’t need
```

#### usePrevious (task/16)

```diff
-const usePrevious = value => {
+const usePrevious = value => {
+ const previousValue = useValue(); const valueToReturn = previousValue; const newValue = value; if (previousValue !== value) { const store = useStore(); // SetState is used to set State on the class instance.
```

#### usePrevious (task/16)

```diff
-const usePrevious = value => {
+const usePrevious = value => {
+
+    let current = this . previousValue ();
+    let next = this . value ();
+    if ( current === next ) {
+    // No need to set it, because it's already the same.
+    return ;
```

#### usePrevious (task/16)

```diff
-const usePrevious = value => {
+const usePrevious = value => {
+
+    if ( _ . isUndefined (value)) {
+    return store . getters . usePrevious ;
+    }
+    return store . getters . usePrevious . call (store, value);
+    };
+    /**
```

#### useMediaQuery (task/17)

```diff
-const useMediaQuery = (query, whenTrue, whenFalse) => {
+const useMediaQuery = (query, whenTrue, whenFalse) => {
+ const value = mediaQueryList[query] || 0; if (value > 0) { return whenTrue(value); } else { return whenFalse(value); } };
+    And that’s it! We are now ready to
```

#### useMediaQuery (task/17)

```diff
-const useMediaQuery = (query, whenTrue, whenFalse) => {
+const useMediaQuery = (query, whenTrue, whenFalse) => {
+
+    const el = document.createElement('link');
+    el.media = {
+    type: 'all',
+    rel: 'stylesheet',
+    href: `${path}/style.css`
+    };
```

#### useMediaQuery (task/17)

```diff
-const useMediaQuery = (query, whenTrue, whenFalse) => {
+const useMediaQuery = (query, whenTrue, whenFalse) => {
+ let isTrue = false; // do this first, so that when you add a media query to the array, it won't be evaluated as true (allowing you to progressively increase max-width) if (query.matches) { is
```

#### useMediaQuery (task/17)

```diff
-const useMediaQuery = (query, whenTrue, whenFalse) => {
+const useMediaQuery = (query, whenTrue, whenFalse) => {
+
+    const { media } = query;
+    const shouldUseMedia = (srcWidth, srcHeight) =>
+    whenTrue(srcWidth >= media.minWidth && srcHeight >= media.minHeight) ||
+    whenFalse
```

#### useMediaQuery (task/17)

```diff
-const useMediaQuery = (query, whenTrue, whenFalse) => {
+const useMediaQuery = (query, whenTrue, whenFalse) => {
+ return () => { if (query.matches(`only screen and (min-width: ${window.innerWidth})`)) { whenTrue(); } else { whenFalse(); } }; };
+    Alternatively, a function can be returned
```

#### useDefault (task/18)

```diff
-const useDefault = (defaultState, initialState) => {
+const useDefault = (defaultState, initialState) => {
+ let get = key => state => state[key]; let put = (key, value) => state => ({ [key]: value }); let use = (action, callback) => { let default = {}; if (typeof action === '
```

#### useDefault (task/18)

```diff
-const useDefault = (defaultState, initialState) => {
+const useDefault = (defaultState, initialState) => {
+ return { ...defaultState, ...initialState } } const store = compose( connect( useDefault( {} , { users: [] } ), loadUsers ), mapStateToProps, mapDispatchToProps, )(TodoApp)
```

#### useDefault (task/18)

```diff
-const useDefault = (defaultState, initialState) => {
+const useDefault = (defaultState, initialState) => {
+
+    const state = initialState || defaultState;
+    return (state, action) => {
+    switch (action.type) {
+    case 'FETCH_DATA':
+    return fetchData(state, action);
```

#### useDefault (task/18)

```diff
-const useDefault = (defaultState, initialState) => {
+const useDefault = (defaultState, initialState) => {
+ let {defaultState, initialState} = defaultState; defaultState.setState(initialState); return defaultState; }; const reducer = createReducer(initialState, { [actions.SET_STATE] (state, action)
```

#### useDefault (task/18)

```diff
-const useDefault = (defaultState, initialState) => {
+const useDefault = (defaultState, initialState) => {
+
+    const [state, dispatch] = useReducer(
+    reducer,
+    initialState,
+    getProps(defaultState),
+    );
+    return { state, dispatch };
+    };
+    const use
```

#### TagInput (task/19)

```diff
-const TagInput = ({ tags }) => {
+const TagInput = ({ tags }) => {
+ let tagList = []; tags.forEach((tag) => { tagList.push( <span className="tag" key={tag.name}>{tag.name}</span> ); }); return ( <div className="
```

#### TagInput (task/19)

```diff
-const TagInput = ({ tags }) => {
+const TagInput = ({ tags }) => {
+ const input = document . createElement ( 'input' ); input . setAttribute ( 'type' , 'hidden' ); input . setAttribute ( 'name' , 'tags' ); input . setAttribute ( 'value' , Object . keys
```

#### TagInput (task/19)

```diff
-const TagInput = ({ tags }) => {
+const TagInput = ({ tags }) => {
+ const input = input || document . createElement ( 'input' ); const tags = tags || []; return ( < input value = { input . value } onChange = { e => tags . push ( e . target . value )} /> );
```

#### TagInput (task/19)

```diff
-const TagInput = ({ tags }) => {
+const TagInput = ({ tags }) => {
+
+    const [ value , setValue ] = useState ( ' ' );
+    const handleChange = event => {
+    const tag = event . target . value ;
+    setValue ( tag );
+    };
+    return (
```

#### TagInput (task/19)

```diff
-const TagInput = ({ tags }) => {
+const TagInput = ({ tags }) => {
+ return ( < div > < input type = "text" value = { tags } onChange = { e => this . setState ({ tags : e . target . value })} / > < /div > ); };
+    Next, we
```

#### MultiselectCheckbox (task/20)

```diff
-const MultiselectCheckbox = ({ options, onChange }) => {
+const MultiselectCheckbox = ({ options, onChange }) => {
+
+    return (
+    <input
+    type="checkbox"
+    checked={onChange(false)}
+    onChange={onChange}
+    />
+    );
+    };
+    export default MultiselectCheckbox
```

#### MultiselectCheckbox (task/20)

```diff
-const MultiselectCheckbox = ({ options, onChange }) => {
+const MultiselectCheckbox = ({ options, onChange }) => {
+
+    const { checked } = options.values;
+    return (
+    <form onSubmit={onChange}>
+    {Object.keys(options).map(key => {
+    return (
+    <div>
```

#### MultiselectCheckbox (task/20)

```diff
-const MultiselectCheckbox = ({ options, onChange }) => {
+const MultiselectCheckbox = ({ options, onChange }) => {
+ const { checked, isSelected } = options . filter (option => option . selected ) . reduce (( a , b ) => { a . isSelected = b . isSelected || ( a . isSelected && ! b .
```

#### MultiselectCheckbox (task/20)

```diff
-const MultiselectCheckbox = ({ options, onChange }) => {
+const MultiselectCheckbox = ({ options, onChange }) => {
+ const _onChange = onChange; return ( < form > < input type = " checkbox " id = " check " value = { null } onChange = { onChange } /> < div className = " options " > { options
```

#### MultiselectCheckbox (task/20)

```diff
-const MultiselectCheckbox = ({ options, onChange }) => {
+const MultiselectCheckbox = ({ options, onChange }) => {
+ const group = options.group || ''; const label = options.label || ''; const onChangeHandler = (value) => { console.log(value); onChange(value); }; return ( <div> <div className="
```

#### DataList (task/21)

```diff
-const DataList = ({ isOrdered = false, data }) => {
+const DataList = ({ isOrdered = false, data }) => {
+ const data = isOrdered ? data.slice(0, data.length - 1) : data; const isCollapsed = data.length > 10; return ( <div className="list-group"> {isCollapsed && (
```

#### DataList (task/21)

```diff
-const DataList = ({ isOrdered = false, data }) => {
+const DataList = ({ isOrdered = false, data }) => {
+ if (isOrdered) { return ( <Ordered.List data={data} key="data.id" /> ); } return ( <div> <ul> {data.map(item => ( <li key={item.id
```

#### DataList (task/21)

```diff
-const DataList = ({ isOrdered = false, data }) => {
+const DataList = ({ isOrdered = false, data }) => {
+
+    if (isOrdered) {
+    return data.map((d) => {
+    return (<div key={d.id}>{d.name}</div>);
+    });
+    } else {
```

#### DataList (task/21)

```diff
-const DataList = ({ isOrdered = false, data }) => {
+const DataList = ({ isOrdered = false, data }) => {
+ const isValid = isOrdered && !isValid(data); if (isValid) { return { isValid, data }; } else { return { isValid: false, data }; } };
+    To use it, import it into
```

#### DataList (task/21)

```diff
-const DataList = ({ isOrdered = false, data }) => {
+const DataList = ({ isOrdered = false, data }) => {
+ const isOrdered = isOrdered === undefined ? false : isOrdered; const isDragging = false; const isEndReached = false; const _data = data || []; const _dragData = []; const _lastItem
```

#### Carousel (task/22)

```diff
-const Carousel = ({ carouselItems, ...rest }) => {
+const Carousel = ({ carouselItems, ...rest }) => {
+ const carouselItems = carouselItems.concat(...rest); return ( <div className={`flex-container`}> <div className="flex-item" onClick={() => carouselItems.push(0
```

#### Carousel (task/22)

```diff
-const Carousel = ({ carouselItems, ...rest }) => {
+const Carousel = ({ carouselItems, ...rest }) => {
+ const carouselDirection = rest.carouselDirection || 'vertical'; const animationDuration = rest.animationDuration || 300; return ( <div className={'carousel ' + carouselDirection}> {carousel
```

#### Carousel (task/22)

```diff
-const Carousel = ({ carouselItems, ...rest }) => {
+const Carousel = ({ carouselItems, ...rest }) => {
+
+    const { onPaginationClick, onSlideClick, onSlideBefore, onSlideAfter, onSlideNext, onSlidePrev } = rest;
+    return (
+    <CarouselPage
```

#### Carousel (task/22)

```diff
-const Carousel = ({ carouselItems, ...rest }) => {
+const Carousel = ({ carouselItems, ...rest }) => {
+ // ... }
+    When creating a Carousel component, you’ll use the spread operator ( ...rest ) to pass in any additional props or a data object to the Carousel . You can then pass these properties down as props to the
```

#### Carousel (task/22)

```diff
-const Carousel = ({ carouselItems, ...rest }) => {
+const Carousel = ({ carouselItems, ...rest }) => {
+ const [ carousel, carouselItems ] = rest; return ( <div className="carousel"> <div className="carousel-inner"> {carouselItems.map((item, index) => ( <div key={index
```

#### useMergeState (task/23)

```diff
-const useMergeState = (initialState = {}) => {
+const useMergeState = (initialState = {}) => {
+
+    return {
+    ...initialState,
+    user: {
+    ...initialState.user,
+    saved: false
+    }
+    }
+    }
+    A mergeState function is used in reducers to
```

#### useMergeState (task/23)

```diff
-const useMergeState = (initialState = {}) => {
+const useMergeState = (initialState = {}) => {
+ const mergeState = initialState; const reducer = (state = mergeState, action) => { switch (action.type) { case 'INCREMENT': return mergeState + 1; case 'DECREMENT': return mergeState -
```

#### useMergeState (task/23)

```diff
-const useMergeState = (initialState = {}) => {
+const useMergeState = (initialState = {}) => {
+ const [state, dispatch] = useState(initialState); const mergeState = (nextState, update) => { const { dispatch } = nextState; return { ...state, [dispatch] : mergeDispatch(dispatch, update
```

#### useMergeState (task/23)

```diff
-const useMergeState = (initialState = {}) => {
+const useMergeState = (initialState = {}) => {
+
+    const mergedState = initialState
+    const changedKeys = Object.keys(initialState)
+    .filter(key => !Object.isFrozen(initialState[key]))
+    .map(key => [key
```

#### useMergeState (task/23)

```diff
-const useMergeState = (initialState = {}) => {
+const useMergeState = (initialState = {}) => {
+
+    const mergedState = initialState || {};
+    let actionTypes = [...Array(7)].map(type => typeof type);
+    const actionTypeNames = actionTypes.map(type => type.toLowerCase
```

#### useAsync (task/24)

```diff
-const useAsync = fn => {
+const useAsync = fn => {
+ let __data; return function ( ) { return __data = fn( ); __data && __data(); } } ; const test = async( ) => { const data = await useAsync( ( ) => { let result = await useAsync
```

#### useAsync (task/24)

```diff
-const useAsync = fn => {
+const useAsync = fn => {
+
+    return new Promise (( resolve , reject ) => {
+    let done = false ;
+    fn ( done , resolve , reject );
+    setTimeout (() => {
+    if ( done ) {
+    done ( resolve ,
```

#### useAsync (task/24)

```diff
-const useAsync = fn => {
+const useAsync = fn => {
+
+    if ( typeof fn !== ' function ' ) {
+    throw new TypeError ( ' Expecting a function, got ' +
+    ( typeof fn === ' object ' ?
+    ' an object with a ' +
```

#### useAsync (task/24)

```diff
-const useAsync = fn => {
+const useAsync = fn => {
+ let nextId = 0; return { then: next => { setTimeout(() => { next(nextId++); }, 1000); } }; }; // await 是 Promise.resolve 所提供的
```

#### useAsync (task/24)

```diff
-const useAsync = fn => {
+const useAsync = fn => {
+
+    let result = fn ();
+    if ( ! result . done ) {
+    return function () {
+    result . done = true ;
+    result . value ;
+    };
+    }
+    };
+    function chain
```

#### useBodyScrollLock (task/25)

```diff
-const useBodyScrollLock = () => {
+const useBodyScrollLock = () => {
+ let {main} = window; const body = main.document.body; if (BodyScrollLock.isCurrentlyEnabled()) { return false; } BodyScrollLock.enable(); const bodyScroll = (x) => { const diff = x
```

#### useBodyScrollLock (task/25)

```diff
-const useBodyScrollLock = () => {
+const useBodyScrollLock = () => {
+ setUseBodyScrollLock(true); };
+    setUseBodyScrollLock ( true ) ;
+    } ;
+    } ) ;
+    } ,
+    error : function ( xhr , err , p ) {
+    console
```

#### useBodyScrollLock (task/25)

```diff
-const useBodyScrollLock = () => {
+const useBodyScrollLock = () => {
+
+    if ( this . useBodyScroll ) {
+    this . useBodyScroll = false ;
+    this . bodyScrollOffset = 0 ;
+    }
+    };
+    // Disable scrolling when content is fixed
+    useBody
```

#### useBodyScrollLock (task/25)

```diff
-const useBodyScrollLock = () => {
+const useBodyScrollLock = () => {
+ if (document.body.scrollTop > document.body.scrollHeight - window.innerHeight) { document.body.scrollTop = document.body.scrollHeight - window.innerHeight; } }; </script> </body> </
```

#### useBodyScrollLock (task/25)

```diff
-const useBodyScrollLock = () => {
+const useBodyScrollLock = () => {
+
+    const observer = new MutationObserver(mutation => {
+    if (mutation.attributeName === 'scrollLock' &&
+    mutation.oldValue !== '1' &&
+    mutation.newValue
```

#### useForm (task/26)

```diff
-const useForm = initialValues => {
+const useForm = initialValues => {
+ let form = null; for (let field of initialValues) { if (field.type === 'Number') { form = <input type="number" name={field.name} value={field.value} onChange={this.handle
```

#### useForm (task/26)

```diff
-const useForm = initialValues => {
+const useForm = initialValues => {
+
+    let { setForm, setField } = arguments
+    let {
+    form,
+    errors
+    } = useForm(initialValues)
+    return {
+    form,
+    errors
+    }
+    }
```

#### useForm (task/26)

```diff
-const useForm = initialValues => {
+const useForm = initialValues => {
+
+    const form = createForm();
+    form.onSubmit(newValue => {
+    const currentValues = useValue(initialValues, newValue);
+    const validated = validate(currentValues);
+    // ...
```

#### useForm (task/26)

```diff
-const useForm = initialValues => {
+const useForm = initialValues => {
+ const { email, password } = initialValues; return { email, password }; }; const { email, password } = useForm(initialValues); if (email.trim().length > 0 && password.trim().length > 0)
```

#### useForm (task/26)

```diff
-const useForm = initialValues => {
+const useForm = initialValues => {
+ const { target, ...data } = getState(context); const [input, setInput] = React.useState(initialValues); const checkbox = target.checked ? data.input : null; const getConfig = input => {
```

#### usePortal (task/27)

```diff
-const usePortal = el => {
+const usePortal = el => {
+
+    const target = el . querySelector ( ' .target ' );
+    if ( ! target) {
+    return ;
+    }
+    const [ name , isExact ] = target . getAttribute ( ' data-
```

#### usePortal (task/27)

```diff
-const usePortal = el => {
+const usePortal = el => {
+
+    return el.querySelector('[data-portal]');
+    };
+    const actions = {
+    openPortal: portal => {
+    usePortal(portal).style.display = 'block';
```

#### usePortal (task/27)

```diff
-const usePortal = el => {
+const usePortal = el => {
+
+    const [portal, setPortal] = useValue(el.portal);
+    const [portalScroll, setPortalScroll] = usePortal(el);
+    const [portalKey, setPort
```

#### usePortal (task/27)

```diff
-const usePortal = el => {
+const usePortal = el => {
+
+    return (el.querySelector('a').getAttribute('href') === '#');
+    }
+    const isCurrentPage = path => path.includes('/current')
+    const useCurrentPage = el => {
```

#### usePortal (task/27)

```diff
-const usePortal = el => {
+const usePortal = el => {
+ const testID = el.querySelector(".test-id"); const testName = el.querySelector(".test-name"); const testDescription = el.querySelector(".test-description"); const testButton = el
```

#### Mailto (task/28)

```diff
-const Mailto = ({ email, subject = '', body = '', children }) => {
+const Mailto = ({ email, subject = '', body = '', children }) => {
+
+    return {
+    ...state,
+    ...Mailto.initialState,
+    subject,
+    body,
+    children
+    };
+    };
+    I don’t have to worry about setting the initial state
```

#### Mailto (task/28)

```diff
-const Mailto = ({ email, subject = '', body = '', children }) => {
+const Mailto = ({ email, subject = '', body = '', children }) => {
+ return ( <div className="mailto"> <input type="text" value={email} onChange={e => this.onChange(e)} /> <input type="text" value={subject} onChange={e => this.
```

#### Mailto (task/28)

```diff
-const Mailto = ({ email, subject = '', body = '', children }) => {
+const Mailto = ({ email, subject = '', body = '', children }) => {
+ return ( <div className="mailto"> <p> <a href={`mailto:${email}?subject=${subject}&body=${body}`}>{email}</a> </p> <p
```

#### Mailto (task/28)

```diff
-const Mailto = ({ email, subject = '', body = '', children }) => {
+const Mailto = ({ email, subject = '', body = '', children }) => {
+ return ( <div className="mailto"> <input type="text" className="input" placeholder="Email" value={email} onChange={(e) => this.setState({ email: e.target.value })}
```

#### Mailto (task/28)

```diff
-const Mailto = ({ email, subject = '', body = '', children }) => {
+const Mailto = ({ email, subject = '', body = '', children }) => {
+
+    const emailRegex = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"
```

#### useKeyPress (task/29)

```diff
-const useKeyPress = targetKey => {
+const useKeyPress = targetKey => {
+
+    const isDown = KeyEvent.isDown(targetKey);
+    const isUp = KeyEvent.isUp(targetKey);
+    return isDown || isUp;
+    };
+    const mouseDown = (target
```

#### useKeyPress (task/29)

```diff
-const useKeyPress = targetKey => {
+const useKeyPress = targetKey => {
+
+    const debouncedFunction = debounce ( targetKey => {
+    if ( hasKey (targetKey)) {
+    if ( window . event ) {
+    event . preventDefault ();
+    event . stopPropagation ();
```

#### useKeyPress (task/29)

```diff
-const useKeyPress = targetKey => {
+const useKeyPress = targetKey => {
+
+    let { value } = props ;
+    const ret = value === true ? ' ' : targetKey;
+    if (ret === targetKey) {
+    return {
+    ... props ,
+    ... action (targetKey
```

#### useKeyPress (task/29)

```diff
-const useKeyPress = targetKey => {
+const useKeyPress = targetKey => {
+ return () => { if (key => { if (key === targetKey) { return true ; } }) return false ; }; }; const modifiers = { alt: useKeyPress( 13 ), shift: useKeyPress( 16 ), control: use
```

#### useKeyPress (task/29)

```diff
-const useKeyPress = targetKey => {
+const useKeyPress = targetKey => {
+
+    if ( ! targetKey) {
+    return false ;
+    }
+    const handler = {
+    [targetKey] : event => {
+    const { name, ... props } = event.target;
+    if
```

#### CountDown (task/30)

```diff
-const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+ const format = d3.time.format("h:mm:ss"); const now = moment(); let remaining; return ( <div className="countdown"> <div className="col-xs-12"> <div className="
```

#### CountDown (task/30)

```diff
-const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+
+    return (
+    <div className="countdown">
+    <div className="countdown-display">
+    <span className="countdown-hours">{hours}h</span>
+    <span class
```

#### CountDown (task/30)

```diff
-const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+ return <div> <p>{hours} hours</p> <p>{minutes} minutes</p> <p>{seconds} seconds</p> </div>; }; export default CountDown;
+    We could ref
```

#### CountDown (task/30)

```diff
-const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+ if (hours > 0) { return <div>{hours} hour{s} left</div> } if (minutes > 0) { return <div>{minutes} minute{s} left</div> } if (
```

#### CountDown (task/30)

```diff
-const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+ let hours = hours || 12; let minutes = minutes || 60; let seconds = seconds || 0; return ( <div className="countdown"> <span className="counter">{hours} hours {minutes} minutes</span>
```

#### Alert (task/31)

```diff
-const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+ return ( <div className="alert alert-warning"> <button type="button" className="close" onClick={() => this.setState({ isDefaultShown: false })}>×</button> <h4 class
```

#### Alert (task/31)

```diff
-const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+ let showAlert = () => { const dialogRef = this.alertRef; dialogRef.showAlert(type, message, { isDefaultShown: isDefaultShown, timeout }); }; return ( <div> <a href="#"
```

#### Alert (task/31)

```diff
-const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+ const duration = () => { const { isDefaultShown, timeout } = this; if (isDefaultShown) { clearTimeout(timeout); } timeout = setTimeout(duration, timeout); }; const show = () => { isDefault
```

#### Alert (task/31)

```diff
-const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+ const { isDefaultShown, type, message } = options; if (isDefaultShown) { return <div onClick={() => { setTimeout(() => { if (message !== null) { alert(message); }
```

#### Alert (task/31)

```diff
-const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+ const { type, message } = typeof type === 'function' ? type(message) : type; if (isDefaultShown) { return { closeButton: true, closeText: '删除', type: type
```

#### useHash (task/32)

```diff
-const useHash = () => {
+const useHash = () => {
+ const check = new URL(url).searchParams.get(hash) === null; return check; };
+    This will throw an error if the URL does not have a hash, but does work if it does have a hash.
```

#### useHash (task/32)

```diff
-const useHash = () => {
+const useHash = () => {
+ return () => { const query = new URLSearchParams ( window . location . search ) if ( ! query . has ( 'search' )) { return } const [ url , ... rest ] = query . get ( 'search' )
```

#### useHash (task/32)

```diff
-const useHash = () => {
+const useHash = () => {
+
+    const { data , error } = use ( window . fetch );
+    if ( error ) {
+    throw error ;
+    }
+    return { data , error };
+    };
+    const update = ( id , data
```

#### useHash (task/32)

```diff
-const useHash = () => {
+const useHash = () => {
+ console . log ( ' useHash ' ); }; // インスタンスの初期化 const instance = new Instance (); // 呼び出し（コールバック
```

#### useHash (task/32)

```diff
-const useHash = () => {
+const useHash = () => {
+
+    let url = document.location.href;
+    let hash = url.hash;
+    if (hash) {
+    hash = decodeURIComponent(hash);
+    if (hash === '!2') {
```

#### useDelayedState (task/33)

```diff
-const useDelayedState = (initialState, condition) => {
+const useDelayedState = (initialState, condition) => {
+
+    const [state, setState] = useState(initialState);
+    if (condition()) {
+    setState(initialState);
+    }
+    return state;
+    };
+    const createDelayedState =
```

#### useDelayedState (task/33)

```diff
-const useDelayedState = (initialState, condition) => {
+const useDelayedState = (initialState, condition) => {
+
+    const state = initialState
+    const [lastValue, setLastValue] = useState(state)
+    const [state, setState] = useState(state)
+    const [lastAction, setLastAction]
```

#### useDelayedState (task/33)

```diff
-const useDelayedState = (initialState, condition) => {
+const useDelayedState = (initialState, condition) => {
+
+    const [state, setState] = useState(initialState);
+    const callbacks = [];
+    let conditionState = initialState;
+    const promise = new Promise((resolve, reject) => {
+    if
```

#### useDelayedState (task/33)

```diff
-const useDelayedState = (initialState, condition) => {
+const useDelayedState = (initialState, condition) => {
+ let delayedState = initialState; return function delayedFn() { if (condition()) { return delayedState; } else { return delayedState; } } }
+    const useWithErrorState = (initialState, condition, callback) =>
```

#### useDelayedState (task/33)

```diff
-const useDelayedState = (initialState, condition) => {
+const useDelayedState = (initialState, condition) => {
+
+    const [state, setState] = useState(initialState);
+    const [action, dispatch] = useAction(condition);
+    return {
+    ...state,
+    [action](data) {
+    if
```

#### useSearchParam (task/34)

```diff
-const useSearchParam = param => {
+const useSearchParam = param => {
+
+    const { name, value } = param;
+    return name === 'search' && value === 'true';
+    };
+    }
+    }
+    
+    // Test the use of the create-react-app test environment
```

#### useSearchParam (task/34)

```diff
-const useSearchParam = param => {
+const useSearchParam = param => {
+ const [value, setValue] = param.split('=') let [key, setKey] = value.split('&') // Add a description field if it is not present if (!key) { const description = new SearchParams
```

#### useSearchParam (task/34)

```diff
-const useSearchParam = param => {
+const useSearchParam = param => {
+ const [searchQuery, setSearchQuery] = param.split('?'); return setSearchQuery ? searchQuery : '#&?from=post_tag'; }; const useIndex = (state, action) => { const newState =
```

#### useSearchParam (task/34)

```diff
-const useSearchParam = param => {
+const useSearchParam = param => {
+ let { searchParam } = param ; return searchParam || '' ; } ; useSearchParam ( { searchParam : 'hello' } ) ; useSearchParam ( { searchParam : { hello : 'what' } } ) ;
```

#### useSearchParam (task/34)

```diff
-const useSearchParam = param => {
+const useSearchParam = param => {
+
+    return param.split('=').shift() || 'true';
+    };
+    const searchQuery = value =>
+    useSearchParam(value) ?
+    `${String(value).trim()} {query}
```

#### useUpdate (task/35)

```diff
-const useUpdate = () => {
+const useUpdate = () => {
+ return { type: types.DELETE_TODO, payload: { id } }; }; // No payload is required for the update. const destroyTodo = id => { return { type: types.DELETE_TOD
```

#### useUpdate (task/35)

```diff
-const useUpdate = () => {
+const useUpdate = () => {
+
+    if ( ! this . $scope . $id ) {
+    this . $scope . $id = 1 ;
+    }
+    this . $rootScope . $broadcast ( ' use ' , this . $scope .
```

#### useUpdate (task/35)

```diff
-const useUpdate = () => {
+const useUpdate = () => {
+
+    const n = useReducer (reducer, initialState);
+    if ( n . isValid ) {
+    // use it
+    return n;
+    }
+    // try reducer again
+    return useRed
```

#### useUpdate (task/35)

```diff
-const useUpdate = () => {
+const useUpdate = () => {
+
+    const update = () => {
+    const me = this ;
+    me . x += 1 ;
+    me . y += 1 ;
+    };
+    return function ( input ) {
+    const state = { x :
```

#### useUpdate (task/35)

```diff
-const useUpdate = () => {
+const useUpdate = () => {
+
+    this . useBigNumber ();
+    this . useHelper ();
+    this . useQuery ();
+    this . useView ();
+    }
+    it ( ' has to check for extend mode ' , () => {
```

#### Select (task/36)

```diff
-const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+ const onSelect = (index) => { const value = values[index]; selectedValue = value; onValueChange(value); }; return ( <div> <div>{values.map( (value, index) => ( <div
```

#### Select (task/36)

```diff
-const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+
+    const {
+    [thrown] : onValueChangeThrown
+    } = values;
+    return (
+    <div>
+    <Select.Input value={selectedValue} onChange={onValueChange} />
```

#### Select (task/36)

```diff
-const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+ let value = null; if (onValueChange) { value = onValueChange(values); } if (selectedValue) { value = selectedValue; } return { value, onChange(value) { onValueChange(value); },
```

#### Select (task/36)

```diff
-const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+ const [selectedValue, setSelectedValue] = rest; const getValue = () => values[selectedValue]; return ( <div> <div className="select-wrapper"> <div className="select-input"> <label html
```

#### Select (task/36)

```diff
-const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+ const { onValueChange, selectedValue } = rest return ( <div> <h2>Select</h2> <div> <p> {values.join(', ')} </p> <span onClick={onValueChange
```

#### LimitedWordTextarea (task/37)

```diff
-const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+ let { rows, cols, value, limit } = this.props return ( <div className="textarea"> <div className="textarea-preview"> {JSON.stringify(value, null, 2)} </
```

#### LimitedWordTextarea (task/37)

```diff
-const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+ const rows = Math.max(Math.ceil(cols / 10), 2); const cols = Math.max(rows / 10, 20); const value = value.toString().split('').reverse().join(''
```

#### LimitedWordTextarea (task/37)

```diff
-const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+ const numChars = value.length; const minChars = rows * cols; const maxChars = Math.ceil(numChars / limit); return ( <div className="textarea-wrapper"> <div class
```

#### LimitedWordTextarea (task/37)

```diff
-const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+ return { cols: cols, rows: rows, value: value, limit: limit } } // Validate the length of the input const validateLength = (input) => { const rows = input.rows const cols = input.
```

#### LimitedWordTextarea (task/37)

```diff
-const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+ let textarea = value || ''; if (rows && cols) { return textarea.split( '
+    ' ).map(line => { if (line.length <= limit) { return line; } else { return ` ${
```

#### useOnWindowScroll (task/38)

```diff
-const useOnWindowScroll = callback => {
+const useOnWindowScroll = callback => {
+
+    const host = document.activeElement;
+    if (host) {
+    callback();
+    }
+    };
+    const useOnMouseMove = callback => {
+    const el = event.target;
+    if
```

#### useOnWindowScroll (task/38)

```diff
-const useOnWindowScroll = callback => {
+const useOnWindowScroll = callback => {
+ // callback(true); // callback(false); // callback(0); // callback(2147483647); // callback(0, "something"); // callback(0, null); // callback(0, undefined); // callback(0
```

#### useOnWindowScroll (task/38)

```diff
-const useOnWindowScroll = callback => {
+const useOnWindowScroll = callback => {
+
+    const r = callback ( document . documentElement , ' scroll ' );
+    return r;
+    };
+    const useOnWebMouseScroll = callback => {
+    const r = callback ( document . documentElement , ' web
```

#### useOnWindowScroll (task/38)

```diff
-const useOnWindowScroll = callback => {
+const useOnWindowScroll = callback => {
+
+    document . addEventListener ( 'scroll' , callback)
+    }
+    function toggleUseOnWindowScroll () {
+    useOnWindowScroll . cancel ()
+    useOnWindowScroll . currentTarget . removeEventListener (
```

#### useOnWindowScroll (task/38)

```diff
-const useOnWindowScroll = callback => {
+const useOnWindowScroll = callback => {
+
+    const beforeWindowScroll = callback ();
+    const windowRef = window . _UIReady ? window . _UIReady . bind ( window ) : window ;
+    windowRef . scroll ( 0 , windowRef .
```

#### useClickInside (task/39)

```diff
-const useClickInside = (ref, callback) => {
+const useClickInside = (ref, callback) => {
+
+    let previousKey;
+    const isDown = () => {
+    if (previousKey === undefined) {
+    previousKey = ref.current;
+    }
+    return previousKey === ref.current;
```

#### useClickInside (task/39)

```diff
-const useClickInside = (ref, callback) => {
+const useClickInside = (ref, callback) => {
+
+    const useClickOutside = (ref, callback) => {
+    const useClickX = (ref, callback) => {
+    const useClickY = (ref, callback) => {
+    const useClickXOutside =
```

#### useClickInside (task/39)

```diff
-const useClickInside = (ref, callback) => {
+const useClickInside = (ref, callback) => {
+ var onMouseDown = useState(true); var onMouseUp = useState(false); var onMouseMove = useState(0); const [onMouseDown, onMouseUp] = useRef(onMouseDown, onMouse
```

#### useClickInside (task/39)

```diff
-const useClickInside = (ref, callback) => {
+const useClickInside = (ref, callback) => {
+
+    let [{key, ...data}] = ref.get();
+    const handle = data[key];
+    if (handle) {
+    callback(handle);
+    }
+    };
+    function mapStateTo
```

#### useClickInside (task/39)

```diff
-const useClickInside = (ref, callback) => {
+const useClickInside = (ref, callback) => {
+
+    if (ref.currentItem.children[0]._clickable) {
+    return callback();
+    }
+    else {
+    ref.currentItem.children[0]._clickable = true;
+    return
```

#### useSSR (task/40)

```diff
-const isDOMavailable = !!(
+const isDOMavailable = !!(
+() => DOM.document.createElement("div"));
+    const isWebSocketAvailable = !!(() => new WebSocket("ws://localhost:8080"));
+    const isMessageChannelAvailable = !!(() => new Message
```

#### useSSR (task/40)

```diff
-const isDOMavailable = !!(
+const isDOMavailable = !!(
+window.DOM && window.document);
+    1.1.6.1.6. Opera
+    document.all is not supported.
+    is not supported. navigator.appCodeName is not supported.
+    is not
```

#### useSSR (task/40)

```diff
-const isDOMavailable = !!(
+const isDOMavailable = !!(
+kVersionNumber & 0x800000);
+    3109 if (!isDOMavailable)
+    3110 return nullptr ;
+    3111
+    3112 if (isDOMavailable) {
+    3113 if (compiler
```

#### useSSR (task/40)

```diff
-const isDOMavailable = !!(
+const isDOMavailable = !!(
+window.document.createElement && window.document.createEvent && window.document.getElementById && window.navigator.mimeTypes && document.implementation && document.implementation.createDocument);
+    The script checks whether
```

#### useSSR (task/40)

```diff
-const isDOMavailable = !!(
+const isDOMavailable = !!(
+window.document && document.createElement && document.createEvent && window.XMLHttpRequest); const isPointerAvailable = !!window.PointerEvent; const isMouseAvailable = !!window.MouseEvent; const isKeyboardAvailable
```

#### LimitedTextarea (task/41)

```diff
-const LimitedTextarea = ({ rows, cols, value, limit }) => {
+const LimitedTextarea = ({ rows, cols, value, limit }) => {
+ const ROWS = rows || 10; const COLS = cols || 100; const textarea = document.createElement('textarea'); textarea.style.width = `${COLS}px`; textarea.style.height
```

#### LimitedTextarea (task/41)

```diff
-const LimitedTextarea = ({ rows, cols, value, limit }) => {
+const LimitedTextarea = ({ rows, cols, value, limit }) => {
+ let value = value.split('
+    '); // Strips out all lines except the first and last let result = [ value[0], value[value.length - 1] ]; // Gets the total amount of rows and columns let rows =
```

#### LimitedTextarea (task/41)

```diff
-const LimitedTextarea = ({ rows, cols, value, limit }) => {
+const LimitedTextarea = ({ rows, cols, value, limit }) => {
+ const onChange = e => { const { value } = e.target const { rows, cols } = this.props const len = value.length if (value.length > limit) { value = value.slice(0,
```

#### LimitedTextarea (task/41)

```diff
-const LimitedTextarea = ({ rows, cols, value, limit }) => {
+const LimitedTextarea = ({ rows, cols, value, limit }) => {
+ let max = rows * cols; return ( <div> <p>You have ${max} characters left.</p> <textarea rows={rows} cols={cols} value={value} onChange={(event) =>
```

#### LimitedTextarea (task/41)

```diff
-const LimitedTextarea = ({ rows, cols, value, limit }) => {
+const LimitedTextarea = ({ rows, cols, value, limit }) => {
+ const rows = rows || 16; const cols = cols || 32; return ( <div className="textarea"> <textarea className="textarea col s12" rows={rows} cols={cols} value={
```

#### useComponentDidMount (task/42)

```diff
-const useComponentDidMount = onMountHandler => {
+const useComponentDidMount = onMountHandler => {
+ this.setState({ isInitialMount: true }); window.setInterval(() => { if (this.state.isInitialMount) { this.setState({ isInitialMount: false }); } }, 1000); }; const useEffect
```

#### useComponentDidMount (task/42)

```diff
-const useComponentDidMount = onMountHandler => {
+const useComponentDidMount = onMountHandler => {
+
+    console . log ( 'Did mount' );
+    // ...
+    }
+    const useComponentWillUpdate = onUpdateHandler => {
+    console . log ( 'Will update' );
+    // ...
+    }
```

#### useComponentDidMount (task/42)

```diff
-const useComponentDidMount = onMountHandler => {
+const useComponentDidMount = onMountHandler => {
+
+    if ( component ) {
+    component . useEffect ( ( ) => {
+    if ( component . useContext ) {
+    component . useContext ( 'foo' ) ;
+    }
+    component . onMountHandler
```

#### useComponentDidMount (task/42)

```diff
-const useComponentDidMount = onMountHandler => {
+const useComponentDidMount = onMountHandler => {
+
+    document.addEventListener('click', () => {
+    // Do something.
+    })
+    return () => {
+    document.removeEventListener('click', onMountHandler)
+    }
+    }
```

#### useComponentDidMount (task/42)

```diff
-const useComponentDidMount = onMountHandler => {
+const useComponentDidMount = onMountHandler => {
+ const { setState } = onMountHandler . context ; setState ( { myState : { foo : ' bar ' } } ) ; } ; const { setState } = onMountHandler . context ; const useReducer = ( state
```

#### FileDrop (task/43)

```diff
-const FileDrop = ({ onDrop }) => {
+const FileDrop = ({ onDrop }) => {
+ return { dragOver : onDrop ( _ => false ), drop : onDrop ( _ => { // ドラッグ終了時に、ファイルの追加をアニメーショ
```

#### FileDrop (task/43)

```diff
-const FileDrop = ({ onDrop }) => {
+const FileDrop = ({ onDrop }) => {
+
+    return {
+    onDragEnter ( e ) {
+    // If the file is moved on to this element, it means that it
+    // should be loaded.
+    // If the file is dragged in past this element,
```

#### FileDrop (task/43)

```diff
-const FileDrop = ({ onDrop }) => {
+const FileDrop = ({ onDrop }) => {
+ return { draggable : true , onDrop : onDrop }; }; export default FileDrop ;
+    What we're doing here is just creating a custom component using a render prop, which will then be imported into the App component where we'll
```

#### FileDrop (task/43)

```diff
-const FileDrop = ({ onDrop }) => {
+const FileDrop = ({ onDrop }) => {
+ return class WithDrop extends React . Component { onDrop = onDrop; render () { return ( < div onClick = { this . onDrop } > Drop Files Here < / div > ); } }; };
+    You can now use the
```

#### FileDrop (task/43)

```diff
-const FileDrop = ({ onDrop }) => {
+const FileDrop = ({ onDrop }) => {
+
+    onDrop = onDrop || noop;
+    return class extends React.Component {
+    state = {
+    file: {
+    type: null,
+    name: null,
+    },
+    };
```

#### TreeView (task/44)

```diff
-const TreeView = ({
+const TreeView = ({
+ items, view }) => { return ( <div> <ul> {items.map((item, index) => ( <li key={index}> <TreeItem key={item.id} item={item} /> </li> ))
```

#### TreeView (task/44)

```diff
-const TreeView = ({
+const TreeView = ({
+ id, level }) => ( <View style={styles.treeview}> <View style={styles.treeview_contents}> <View style={styles.treeview_contents_header}> <Text style={styles.
```

#### TreeView (task/44)

```diff
-const TreeView = ({
+const TreeView = ({
+ children, hidden, selected, userFocus, userActive }) => { // nothing to do in the constructor return class extends React.Component { render() { return ( <div> <div> <h2>{hidden ? 'Hidden' :
```

#### TreeView (task/44)

```diff
-const TreeView = ({
+const TreeView = ({
+ action, onChange, ...rest }) => ( < div > < select onChange = {onChange} > {rest} </ select > < button onClick = {action} > Change </ button > </ div > ); export default TreeView
```

#### TreeView (task/44)

```diff
-const TreeView = ({
+const TreeView = ({
+ items }) => ( < div > { items . map ( item => < div > < h3 > { item . text } < /h3> < /div> )} < /div> ); // If a prop is passed, we
```

#### usePersistedState (task/45)

```diff
-const usePersistedState = (name, defaultValue) => {
+const usePersistedState = (name, defaultValue) => {
+ // ... }; const useState = (initialState, [usePersistedState]) => { // ... };
+    You could also use useState in combination with useReducer to build a Redux-like state management library.
+    How do
```

#### usePersistedState (task/45)

```diff
-const usePersistedState = (name, defaultValue) => {
+const usePersistedState = (name, defaultValue) => {
+
+    const storage = storage.get(name);
+    if (storage) {
+    return storage.getItem(name);
+    }
+    return defaultValue;
+    };
+    // Return the actual value from the storage
```

#### usePersistedState (task/45)

```diff
-const usePersistedState = (name, defaultValue) => {
+const usePersistedState = (name, defaultValue) => {
+
+    const state = useState(defaultValue);
+    const persistedState = useCallback(() => {
+    state.replace(name, useReducer(name, state));
+    }, [name]);
+    return persistedState
```

#### usePersistedState (task/45)

```diff
-const usePersistedState = (name, defaultValue) => {
+const usePersistedState = (name, defaultValue) => {
+ if (persistedState[name] !== undefined) { return persistedState[name]; } return defaultValue; }; this.setPersistedState = (name, value) => { if (persistedState[name] === undefined)
```

#### usePersistedState (task/45)

```diff
-const usePersistedState = (name, defaultValue) => {
+const usePersistedState = (name, defaultValue) => {
+
+    const val = localStorage.getItem(name) || defaultValue
+    return val !== undefined ? val : defaultValue
+    }
+    /**
+    * Create a store from given state.
+    * @param {
```

#### useWindowSize (task/46)

```diff
-const useWindowSize = () => {
+const useWindowSize = () => {
+
+    const {
+    winWidth,
+    winHeight
+    } = await window.matchMedia('(max-width: 500px)');
+    return { width: winWidth, height: winHeight };
+    };
```

#### useWindowSize (task/46)

```diff
-const useWindowSize = () => {
+const useWindowSize = () => {
+ const {width, height} = window.innerWidth; return useWindowSize; }
+    const useWindowSize = require('./useWindowSize');
+    import { useWindowSize } from './useWindowSize';
```

#### useWindowSize (task/46)

```diff
-const useWindowSize = () => {
+const useWindowSize = () => {
+ const DOM = React.createElement('div', { style: { width: '100%', height: '100%' } }, document.body); ReactDOM.render(DOM, null); }; const useWindowSize = () => {
```

#### useWindowSize (task/46)

```diff
-const useWindowSize = () => {
+const useWindowSize = () => {
+ const [ w , h ] = window . innerWidth , window . innerHeight ; return { w , h }; }; const useWindowSize = () => { const [ w , h ] = window . innerWidth , window . innerHeight ; return
```

#### useWindowSize (task/46)

```diff
-const useWindowSize = () => {
+const useWindowSize = () => {
+
+    const { center, width, height } = useWindowSize();
+    return center + 'px ' + width + 'px ' + height + 'px';
+    };
+    const makeImage = input => `
+    <
```

#### ControlledInput (task/47)

```diff
-const ControlledInput = ({ value, onValueChange, ...rest }) => {
+const ControlledInput = ({ value, onValueChange, ...rest }) => {
+
+    const [inputValue, setInputValue] = useState(value);
+    const [onChange, setOnChange] = useState(() => {});
+    const [onBlur, setOnBlur] =
```

#### ControlledInput (task/47)

```diff
-const ControlledInput = ({ value, onValueChange, ...rest }) => {
+const ControlledInput = ({ value, onValueChange, ...rest }) => {
+ const [ checked, setChecked ] = useState(value) let onChange = e => setChecked(e.target.checked) const render = () => ( <div> <label htmlFor="checkbox-example-input
```

#### ControlledInput (task/47)

```diff
-const ControlledInput = ({ value, onValueChange, ...rest }) => {
+const ControlledInput = ({ value, onValueChange, ...rest }) => {
+ ...rest }
+    const el = document.createElement('input')
+    const onChange = (e) => { ... }
+    const ControlledInput = ({ value, onValueChange, ...rest }) => {
+    el.
```

#### ControlledInput (task/47)

```diff
-const ControlledInput = ({ value, onValueChange, ...rest }) => {
+const ControlledInput = ({ value, onValueChange, ...rest }) => {
+ return Controlled.of( { value: value, onValueChange: onValueChange, ...rest }, ) }
+    As a result, we can remove the function call from our application model, thus creating more readable code.
+    const application
```

#### ControlledInput (task/47)

```diff
-const ControlledInput = ({ value, onValueChange, ...rest }) => {
+const ControlledInput = ({ value, onValueChange, ...rest }) => {
+ // lets use the input if value is truthy return onValueChange && <input {...rest} value={value} />; }; ControlledInput.propTypes = { value: PropTypes.bool.isRequired, onValueChange: Prop
```

#### DataTable (task/48)

```diff
-const DataTable = ({ data }) => {
+const DataTable = ({ data }) => {
+ let dataTable = this.table = new DataTable(data); return dataTable; }; DataTable.prototype.columns = [ { header: 'Titel', dataIndex: 'Titel' }, { header: 'ID
```

#### DataTable (task/48)

```diff
-const DataTable = ({ data }) => {
+const DataTable = ({ data }) => {
+ let columns = [...Array(data.length)].map(d => d.name); let dataTable = new DataTable(); dataTable.addColumns(columns); dataTable.addRows(data); return dataTable;
```

#### DataTable (task/48)

```diff
-const DataTable = ({ data }) => {
+const DataTable = ({ data }) => {
+ let rows = []; return ( <table id="my-data-table"> <thead> <tr> <th>Name</th> <th>Age</th> </tr> </thead> <tbody> {rows
```

#### DataTable (task/48)

```diff
-const DataTable = ({ data }) => {
+const DataTable = ({ data }) => {
+
+    return (
+    <div>
+    <h1>Data Table</h1>
+    <table>
+    <thead>
+    <tr>
+    <th>Name</th>
+    <th
```

#### DataTable (task/48)

```diff
-const DataTable = ({ data }) => {
+const DataTable = ({ data }) => {
+ const filter = data.filter || []; return ( <table> <thead> <tr> <th> #{filter.length ? `${filter.join(',')}` : 'No Results'} </th> </tr
```

#### useComponentWillUnmount (task/49)

```diff
-const useComponentWillUnmount = onUnmountHandler => {
+const useComponentWillUnmount = onUnmountHandler => {
+ if (onUnmountHandler) { console . log ( ' Use componentWillUnmount handler ' ); } };
+    Example
+    import { useState } from ' react-native-use-state ' ; import React , { Component }
```

#### useComponentWillUnmount (task/49)

```diff
-const useComponentWillUnmount = onUnmountHandler => {
+const useComponentWillUnmount = onUnmountHandler => {
+
+    if ( onUnmountHandler && onUnmountHandler () === false ) {
+    ReactDOM . unmountComponentAtNode ( this . getDOMNode ());
+    }
+    };
+    useEffect (() => {
```

#### useComponentWillUnmount (task/49)

```diff
-const useComponentWillUnmount = onUnmountHandler => {
+const useComponentWillUnmount = onUnmountHandler => {
+
+    useEffect(() => {
+    if (onUnmountHandler) {
+    const [unmountComponent, setUnmountComponent] = useCallback(() => {
+    if (onUnmountHandler) {
```

#### useComponentWillUnmount (task/49)

```diff
-const useComponentWillUnmount = onUnmountHandler => {
+const useComponentWillUnmount = onUnmountHandler => {
+ if ( componentWillUnmount ) { componentWillUnmount ( ) ; } if ( ! componentWillUnmount ) { onUnmountHandler ( ) ; } } ; import { useState , useCallback } from 'react' ; import {
```

#### useComponentWillUnmount (task/49)

```diff
-const useComponentWillUnmount = onUnmountHandler => {
+const useComponentWillUnmount = onUnmountHandler => {
+
+    const component = onUnmountHandler.context;
+    if (component && component.use) {
+    component.use();
+    }
+    };
+    /**
+    * @interface
+    * @name ReactUp
```

#### Tabs (task/50)

```diff
-const TabItem = props => <div {...props} />;
-
-const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+const TabItem = props => <div {...props} />;
+
+const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+
+    const p = (props) => (
+    <TabItem
+    key={props.index}
+    index={props.index}
+    onTabClick={onTabClick}
+    {...props
```

#### Tabs (task/50)

```diff
-const TabItem = props => <div {...props} />;
-
-const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+const TabItem = props => <div {...props} />;
+
+const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+
+    const { getByName } = indexByName;
+    const tabIndex = getByName(defaultIndex);
+    const { getTabIndex, getTabName } = tabIndex;
+    const { index, value }
```

#### Tabs (task/50)

```diff
-const TabItem = props => <div {...props} />;
-
-const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+const TabItem = props => <div {...props} />;
+
+const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+
+    const getTab = id => id === defaultIndex ? undefined : id;
+    const getIndex = id => id === defaultIndex ? -1 : id;
+    const getChildren = id => getTab(id) !==
```

#### Tabs (task/50)

```diff
-const TabItem = props => <div {...props} />;
-
-const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+const TabItem = props => <div {...props} />;
+
+const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+
+    const tab = '#tabs-container';
+    const tabs = [];
+    return (
+    <div>
+    <div className="tabs">
+    {tabs.map((tab, index) =>
```

#### Tabs (task/50)

```diff
-const TabItem = props => <div {...props} />;
-
-const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+const TabItem = props => <div {...props} />;
+
+const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+
+    const [index, setIndex] = useState(defaultIndex);
+    const { show, hide } = useState(false);
+    const onClick = e => {
+    const { index } = e.target;
```

#### useNavigatorOnLine (task/51)

```diff
-const getOnLineStatus = () =>
+const getOnLineStatus = () =>
+ $ ( ' .slider .on ' ). text () === ' Offline ' ;
+    const getOnLineStatus = () => $ ( ' .slider .on ' ). text () === ' 光纤线
```

#### useNavigatorOnLine (task/51)

```diff
-const getOnLineStatus = () =>
+const getOnLineStatus = () =>
+
+    getLogger()
+    .message("Getting online status...")
+    .info("On-line status: " + onLineStatus);
+    The only difference between them is that the first one returns a Promise, while the
```

#### useNavigatorOnLine (task/51)

```diff
-const getOnLineStatus = () =>
+const getOnLineStatus = () =>
+ { const { isOnline } = firebase . firestore . document ( 'statuses' ) if ( isOnline ) { return 'online' } else { return 'offline' } } const getNickname = firebase . firestore
```

#### useNavigatorOnLine (task/51)

```diff
-const getOnLineStatus = () =>
+const getOnLineStatus = () =>
+ ({offline: false});
+    
+Next, let's update the state by adding a new method named updateStatus:
+    updateStatus = (status) => {
+    this.setState({
+    status: status
+    });
```

#### useNavigatorOnLine (task/51)

```diff
-const getOnLineStatus = () =>
+const getOnLineStatus = () =>
+ { const status = statusText.substring(0, statusText.length - 4); const onLine = status === 'online'; return { onLine, status }; }; module.exports = { getOnLineStatus };
+    This
```

#### PasswordRevealer (task/52)

```diff
-const PasswordRevealer = ({ value }) => {
+const PasswordRevealer = ({ value }) => {
+ const [ input , show ] = value . split ( ' ' ); return ( < div > < div > Type password < input ref = { node => node . focus ()} value = { input } onChange = { event => show ? event
```

#### PasswordRevealer (task/52)

```diff
-const PasswordRevealer = ({ value }) => {
+const PasswordRevealer = ({ value }) => {
+ const status = value === "done" ? "done" : "to-do" ; return < div > < span > { status } </ span > < input onChange = { event => { this . setState ({ value : event .
```

#### PasswordRevealer (task/52)

```diff
-const PasswordRevealer = ({ value }) => {
+const PasswordRevealer = ({ value }) => {
+ const [ _ , value ] = value . split ( ':' ) return value || _ } const req = new XMLHttpRequest () req . open ( 'GET' , '/api/password' , true ) req . setRequestHeader ( '
```

#### PasswordRevealer (task/52)

```diff
-const PasswordRevealer = ({ value }) => {
+const PasswordRevealer = ({ value }) => {
+ let { type, value } = value; return ( <button onClick={type === 'Password'? 'reveal' : 'hide'} type={type} value={value}> {type === 'Password'? value : ''} </
```

#### PasswordRevealer (task/52)

```diff
-const PasswordRevealer = ({ value }) => {
+const PasswordRevealer = ({ value }) => {
+ return ( < div > < input value = { value } onChange = { ( e ) => this . onChange ( e ) } /> < label > { this . getPassword ()} < /label > < /div > ); }; Password
```

#### StarRating (task/53)

```diff
-const Star = ({ marked, starId }) => {
+const Star = ({ marked, starId }) => {
+ const className = marked ? 'star' : ''; return ( <button type="button" className={className} onClick={() => starId(starId)}> <i className="fa fa-star" aria
```

#### StarRating (task/53)

```diff
-const Star = ({ marked, starId }) => {
+const Star = ({ marked, starId }) => {
+ return ( <TouchableOpacity onPress={() => this.props.marked(true, starId)}> <View style={styles.star}> <Text style={styles.name}>{this.props.star
```

#### StarRating (task/53)

```diff
-const Star = ({ marked, starId }) => {
+const Star = ({ marked, starId }) => {
+ return <Star key={starId} marked={marked} />; };
+    The container pattern
+    You might be familiar with the container pattern from React. It is a way to wrap the state of a component in a parent component and pass
```

#### StarRating (task/53)

```diff
-const Star = ({ marked, starId }) => {
+const Star = ({ marked, starId }) => {
+ return ( <div className="star"> <img src={ marked ? markedImage : altImage } alt="star" /> <strong>{ starId }</strong> </div> ); }; export default Star;
+    Now let
```

#### StarRating (task/53)

```diff
-const Star = ({ marked, starId }) => {
+const Star = ({ marked, starId }) => {
+ const { onChange } = this.props; return ( <span className="star" onClick={onChange} {...this.props} /> ); };
+    All we have done here is added some new props to our
```

#### useComponentDidUpdate (task/54)

```diff
-const useComponentDidUpdate = (callback, condition) => {
+const useComponentDidUpdate = (callback, condition) => {
+ // Your updated component will be returned to this callback. return () => { // Only re-render if `condition` evaluates to true. // Note: This is just an example. Use shouldComponentUpdate() // or PureComponent instead. if (
```

#### useComponentDidUpdate (task/54)

```diff
-const useComponentDidUpdate = (callback, condition) => {
+const useComponentDidUpdate = (callback, condition) => {
+ // `useEffect` guarantees that `callback` runs after the first update of the component. // Even if `callback` or `condition` causes an update, the current value of the local variables of the component will be used. // It is
```

#### useComponentDidUpdate (task/54)

```diff
-const useComponentDidUpdate = (callback, condition) => {
+const useComponentDidUpdate = (callback, condition) => {
+
+    const instance = ReactDOM.findDOMNode(this);
+    if (condition.call(instance)) {
+    callback.call(instance);
+    }
+    };
+    export default useComponentDidUpdate;
```

#### useComponentDidUpdate (task/54)

```diff
-const useComponentDidUpdate = (callback, condition) => {
+const useComponentDidUpdate = (callback, condition) => {
+
+    if (condition()) {
+    callback();
+    }
+    };
+    // 3. Render
+    const render = (component, ) => {
+    component.once('didMount', () => {
+    // 4
```

#### useComponentDidUpdate (task/54)

```diff
-const useComponentDidUpdate = (callback, condition) => {
+const useComponentDidUpdate = (callback, condition) => {
+
+    const instance = ReactDOM.findDOMNode(this);
+    if (instance) {
+    instance.addEventListener(
+    condition,
+    () => {
+    callback(instance);
+    },
+    false
```

#### Toggle (task/55)

```diff
-const Toggle = ({ defaultToggled = false }) => {
+const Toggle = ({ defaultToggled = false }) => {
+ return ( < div > < div > < button type = "button" onClick = {() => toggle . defaultToggled = ! toggle . defaultToggled } > { toggle . defaultToggled ? 'ON' : '
```

#### Toggle (task/55)

```diff
-const Toggle = ({ defaultToggled = false }) => {
+const Toggle = ({ defaultToggled = false }) => {
+ return { render : function () { if ( this . defaultToggled ) { return < input type = "checkbox" defaultChecked = { this . defaultToggled } /> } else { return < input type = "checkbox
```

#### Toggle (task/55)

```diff
-const Toggle = ({ defaultToggled = false }) => {
+const Toggle = ({ defaultToggled = false }) => {
+ const { toggled } = this.props.onToggleChange const { show } = this.props.children if (toggled === false) { show = true } else { show = false } return ( <button
```

#### Toggle (task/55)

```diff
-const Toggle = ({ defaultToggled = false }) => {
+const Toggle = ({ defaultToggled = false }) => {
+ return ( < div > < button onClick = {() => { this . setState ({ defaultToggled : ! this . state . defaultToggled }) }} > Toggle </ button > < p > You have { this . state .
```

#### Toggle (task/55)

```diff
-const Toggle = ({ defaultToggled = false }) => {
+const Toggle = ({ defaultToggled = false }) => {
+ const toggled = !defaultToggled; return ( <div> <h3>Toggle switch</h3> <button onClick={toggleToggled}>Toggle</button> </div> ); };
```

#### MappedTable (task/56)

```diff
-const MappedTable = ({ data, propertyNames }) => {
+const MappedTable = ({ data, propertyNames }) => {
+ const classes = propertyNames.filter(p => p.startsWith('_')); return ( <div className={classes.join(' ')}> { data.map(({ id, value }) => ( <div key={id
```

#### MappedTable (task/56)

```diff
-const MappedTable = ({ data, propertyNames }) => {
+const MappedTable = ({ data, propertyNames }) => {
+ const classNames = propertyNames.map(prop => prop.toLowerCase()); return classNames.join(' '); }; export default MappedTable;
+    Then, we can import it in our component:
+    import { Mapped
```

#### MappedTable (task/56)

```diff
-const MappedTable = ({ data, propertyNames }) => {
+const MappedTable = ({ data, propertyNames }) => {
+ const mappedTable = {}; Object.keys(data).forEach(key => { mappedTable[key] = data[key]; }); return mappedTable; }; const CategoryTable = ({ data, propertyNames }) => { const mappedTable =
```

#### MappedTable (task/56)

```diff
-const MappedTable = ({ data, propertyNames }) => {
+const MappedTable = ({ data, propertyNames }) => {
+ const { propertyNames } = getObjToPropMap (data); return prop (prop (map ( propertyNames ))); };
+    By defining a prop function that takes a path and applies prop to each property on that path, we create a
```

#### MappedTable (task/56)

```diff
-const MappedTable = ({ data, propertyNames }) => {
+const MappedTable = ({ data, propertyNames }) => {
+ const index = _.indexBy(data, propertyNames); return { getItemAtIndex: (_, index) => data[index], setItemAtIndex: (_, index, value) => data[index] = value, getCount
```

#### useEventListener (task/57)

```diff
-const useEventListener = (type, handler, el = window) => {
+const useEventListener = (type, handler, el = window) => {
+ const eventHandler = e => e.target.removeEventListener(type, eventHandler); return el.addEventListener(type, eventHandler, false); }; const mixin = (...mixins) => (...args) => mix
```

#### useEventListener (task/57)

```diff
-const useEventListener = (type, handler, el = window) => {
+const useEventListener = (type, handler, el = window) => {
+ let eventType = type.toLowerCase(); if (typeof el.addEventListener !== 'undefined') { el.addEventListener(eventType, handler, false); } else if (typeof el.attachEvent !
```

#### useEventListener (task/57)

```diff
-const useEventListener = (type, handler, el = window) => {
+const useEventListener = (type, handler, el = window) => {
+
+    if (el) {
+    document.addEventListener(type, handler, false);
+    } else {
+    window.addEventListener(type, handler, false);
+    }
+    };
+    useEvent
```

#### useEventListener (task/57)

```diff
-const useEventListener = (type, handler, el = window) => {
+const useEventListener = (type, handler, el = window) => {
+
+    const special = el.addEventListener;
+    if (special) {
+    special(type, handler);
+    } else {
+    el.attachEvent('on' + type, handler);
+    }
```

#### useEventListener (task/57)

```diff
-const useEventListener = (type, handler, el = window) => {
+const useEventListener = (type, handler, el = window) => {
+ let isHandled = false; // set default for handler, if not given if (!handler) { handler = () => {}; } el.addEventListener(type, handler, {capture: true}); el.addEventListener(
```

#### Callto (task/58)

```diff
-const Callto = ({ phone, children }) => {
+const Callto = ({ phone, children }) => {
+ const { country, format } = window.device.telephony; const [ phone, format ] = Callto.children.map( child => child.attr('value') ); const country = window.navigator.onLine ? 'yes
```

#### Callto (task/58)

```diff
-const Callto = ({ phone, children }) => {
+const Callto = ({ phone, children }) => {
+ return children.filter(callto => callto.phone === phone); }; export default Callto;
+    There are a few things to notice here. First, we defined the Callto component as a function.
+    <Callto phone
```

#### Callto (task/58)

```diff
-const Callto = ({ phone, children }) => {
+const Callto = ({ phone, children }) => {
+ return ( <div className="contact-detail"> <div className="contact-phone"> <div className="contact-phone-container"> <div className="contact-phone-header">{phone}</div> <div
```

#### Callto (task/58)

```diff
-const Callto = ({ phone, children }) => {
+const Callto = ({ phone, children }) => {
+
+    return (
+    <div>
+    <h2>Call to</h2>
+    <div>
+    <button onClick={() => alert(phone)}>
+    Alert
+    </button>
```

#### Callto (task/58)

```diff
-const Callto = ({ phone, children }) => {
+const Callto = ({ phone, children }) => {
+ return children.map(child => <div key={child.id}> <input type="text" value={child.phone} onChange={event => this.handleChange(event.target.value)} /> </div>); };
```

#### useOnWindowResize (task/59)

```diff
-const useOnWindowResize = callback => {
+const useOnWindowResize = callback => {
+
+    const { window } = ReactDOM.findDOMNode(this);
+    if (window.innerWidth > window.innerHeight) {
+    callback();
+    } else {
+    callback(true);
+    }
```

#### useOnWindowResize (task/59)

```diff
-const useOnWindowResize = callback => {
+const useOnWindowResize = callback => {
+
+    // We need to read the innerHTML of a DIV element for the callback
+    // to do its job. It's a bad idea to re-read the DOM because that
+    // triggers expensive layout and paint operations.
```

#### useOnWindowResize (task/59)

```diff
-const useOnWindowResize = callback => {
+const useOnWindowResize = callback => {
+
+    const form = document.querySelector('#form');
+    const childForm = document.querySelector('#child-form');
+    // This is the form that will be attached to the window
+    // when the
```

#### useOnWindowResize (task/59)

```diff
-const useOnWindowResize = callback => {
+const useOnWindowResize = callback => {
+ if (isPointerAvailable()) { if (isPointerAvailable(PointerEventType.pointermove)) { callback(PointerEventType.pointermove); } else if (isPointerAvailable(PointerEventType.pointerdown
```

#### useOnWindowResize (task/59)

```diff
-const useOnWindowResize = callback => {
+const useOnWindowResize = callback => {
+
+    const { width, height } = window.innerWidth;
+    callback(width, height);
+    };
+    const useOnScroll = callback => {
+    const { x, y } = window.scrollY;
```

#### UncontrolledInput (task/60)

```diff
-const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+ const value = new FormControl(); onValueChange(value); return value; }; export const ControlledInput = ({ defaultValue, onValueChange, ...rest }) => { const value = new FormControl(); onValueChange(value); return value
```

#### UncontrolledInput (task/60)

```diff
-const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+
+    const { value } = rest[ 0 ];
+    return < input type = " text " defaultValue = {value} onValueChange = {onValueChange} { ... rest } />;
+    };
+    // The next
```

#### UncontrolledInput (task/60)

```diff
-const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+
+    return {
+    defaultValue,
+    onValueChange,
+    ...rest
+    };
+    };
+    export const ControlledInput = ({ defaultValue, onValueChange, ...rest }) => {
+    return {
```

#### UncontrolledInput (task/60)

```diff
-const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+ const [defaultValue, setDefaultValue] = rest; return { onValueChange: onValueChange, defaultValue, value: defaultValue, ...rest }; }; export const ControlledInput = ({ defaultValue, onValueChange, value: string
```

#### UncontrolledInput (task/60)

```diff
-const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+ const [value, setValue] = rest; const onValueChange = e => setValue(value = e.target.value); return { value, onValueChange }; };
+    We can use that in several different ways, with different
```

#### TextArea (task/61)

```diff
-const TextArea = ({
+const TextArea = ({
+ value, ...rest }) => ( <div className="textarea"> <textarea className="example-textarea" value={value} onChange={e => value = e.target.value} onKeyDown={e => {
```

#### TextArea (task/61)

```diff
-const TextArea = ({
+const TextArea = ({
+ value, error, updateTarget, onChange }) => ( <div> <textarea value={value} onChange={e => onChange(e.target.value)} /> <p>{error ? <p style={{color:
```

#### TextArea (task/61)

```diff
-const TextArea = ({
+const TextArea = ({
+ children, value, editor, onEdit }) => { const { height, value } = editor; const { setValue } = onEdit; return ( <textarea editorState={editor} value={value} onChange={e => setValue
```

#### TextArea (task/61)

```diff
-const TextArea = ({
+const TextArea = ({
+value, onChange, onKeyDown, onKeyUp, ...rest}) => <div> <input type="text" onChange={onChange} value={value}/> <span onKeyDown={onKeyDown} onKeyUp
```

#### TextArea (task/61)

```diff
-const TextArea = ({
+const TextArea = ({
+ input }) => ( < textarea oninput = { input . bind ( this )} value = { input . current . value } oninput = { input . current . bind ( this )} > { input . current . value } < /
```

#### useScript (task/62)

```diff
-const useScript = src => {
+const useScript = src => {
+ const script = document.createElement('script'); script.src = src; document.head.appendChild(script); }; const getScript = url => { const script = document.createElement('script'); script.src = url; document
```

#### useScript (task/62)

```diff
-const useScript = src => {
+const useScript = src => {
+ + let script = document.createElement('script'); + script.src = src; + return script; + }; + + useScript('foo'); + + // Source: https://developer.mozilla.org/en-US/
```

#### useScript (task/62)

```diff
-const useScript = src => {
+const useScript = src => {
+ return new Promise(resolve => { document.querySelector('head').appendChild(src) .then(resolve) }) } const el = document.querySelector('#main') const img = document.createElement('img
```

#### useScript (task/62)

```diff
-const useScript = src => {
+const useScript = src => {
+
+    if ( ! useScript) {
+    return false ;
+    }
+    const { fallback : fallbackSrc } = src;
+    if ( fallbackSrc . length > 0 ) {
+    return {
```

#### useScript (task/62)

```diff
-const useScript = src => {
+const useScript = src => {
+
+    const cacheKey = `${src}-loader`;
+    return {
+    request: request => {
+    if (request.url.includes(cacheKey)) {
+    return request;
+    }
+    return
```

#### useRequestAnimationFrame (task/63)

```diff
-const useRequestAnimationFrame = callback => {
+const useRequestAnimationFrame = callback => {
+ requestAnimationFrame(callback); };
+    This is a very clever fix and saves the developer from having to do any manual scheduling, but it has the potential to cause some serious headaches.
+    The reason is that callbacks can hang around after
```

#### useRequestAnimationFrame (task/63)

```diff
-const useRequestAnimationFrame = callback => {
+const useRequestAnimationFrame = callback => {
+
+    callback ();
+    window . requestAnimationFrame ( callback );
+    };
+    /**
+    * Used to determine if a coordinate has a valid position in the window,
+    * while accounting for scrolling and transforms.
+    *
```

#### useRequestAnimationFrame (task/63)

```diff
-const useRequestAnimationFrame = callback => {
+const useRequestAnimationFrame = callback => {
+ let startTime = Date.now(); while (Date.now() - startTime < 1000) { callback(); } };
+    requestAnimationFrame(useRequestAnimationFrame);
+    This is what we're missing. Without this, the callback
```

#### useRequestAnimationFrame (task/63)

```diff
-const useRequestAnimationFrame = callback => {
+const useRequestAnimationFrame = callback => {
+ // inside useRequestAnimationFrame var callbacks = {}; callbacks[callback] = true; // must be true to use it later (see below) return requestAnimationFrame(callback); }; var animation = useRequestAnimationFrame(callback);
```

#### useRequestAnimationFrame (task/63)

```diff
-const useRequestAnimationFrame = callback => {
+const useRequestAnimationFrame = callback => {
+
+    callback ();
+    return window . requestAnimationFrame ( callback );
+    };
+    requestAnimationFrame (() => {
+    const box = new Box ( 50 , 50 );
+    useBox ( box , render );
```

#### useSet (task/64)

```diff
-const useSet = initialValue => {
+const useSet = initialValue => {
+
+    const set = new Map ();
+    set . set ( initialValue , initialValue );
+    return set ;
+    };
+    const mapSet = useSet ( Map ());
+    const original = mapSet . get ( '
```

#### useSet (task/64)

```diff
-const useSet = initialValue => {
+const useSet = initialValue => {
+
+    const nextValue = useValue (initialValue);
+    const hasChanged = nextValue !== nextValue;
+    if (hasChanged) {
+    nextValue = useValue (nextValue);
+    }
+    return
```

#### useSet (task/64)

```diff
-const useSet = initialValue => {
+const useSet = initialValue => {
+
+    const wrappedValue = new Set (initialValue);
+    const {
+    [ Symbol . iterator ] : () => {
+    return wrappedValue;
+    }
+    } = wrappedValue;
+    return {
+    [
```

#### useSet (task/64)

```diff
-const useSet = initialValue => {
+const useSet = initialValue => {
+
+    const use = set (initialValue);
+    const newInitialValue = use . get ();
+    return { ... use, newInitialValue };
+    };
+    // ---------------------------------------------------------------------------------------------------------------------
+    // Wrap a getter using
```

#### useSet (task/64)

```diff
-const useSet = initialValue => {
+const useSet = initialValue => {
+
+    const [result, set] = useSet(initialValue);
+    return result;
+    }
+    const initialValue = {
+    a: 1,
+    b: 2,
+    c: 3
+    };
```

#### useLocalStorage (task/65)

```diff
-const useLocalStorage = (keyName, defaultValue) => {
+const useLocalStorage = (keyName, defaultValue) => {
+
+    let localStorageKey = keyName.toLowerCase();
+    return (localStorage.getItem(localStorageKey) ||
+    localStorage.getItem(localStorageKey + "__default__") ||
+    local
```

#### useLocalStorage (task/65)

```diff
-const useLocalStorage = (keyName, defaultValue) => {
+const useLocalStorage = (keyName, defaultValue) => {
+ if (localStorage.getItem(keyName)) { return localStorage.getItem(keyName); } else { return defaultValue; } }; const useSessionStorage = (keyName, defaultValue) => { return sessionStorage.get
```

#### useLocalStorage (task/65)

```diff
-const useLocalStorage = (keyName, defaultValue) => {
+const useLocalStorage = (keyName, defaultValue) => {
+
+    const value = localStorage.getItem(keyName);
+    if (value === null) {
+    return defaultValue;
+    }
+    return value;
+    };
+    const getInt = (keyName,
```

#### useLocalStorage (task/65)

```diff
-const useLocalStorage = (keyName, defaultValue) => {
+const useLocalStorage = (keyName, defaultValue) => {
+
+    let localStorageKey = keyName + '-user'
+    // Set localStorageKey to defaultValue or a default value if it's undefined
+    localStorageKey = localStorageKey || defaultValue
+    return localStorageKey
```

#### useLocalStorage (task/65)

```diff
-const useLocalStorage = (keyName, defaultValue) => {
+const useLocalStorage = (keyName, defaultValue) => {
+
+    const useLocalStorage = value => {
+    return new Promise((resolve, reject) => {
+    if (localStorage.getItem(keyName)) {
+    localStorage.setItem(keyName, JSON.
```

#### Collapse (task/66)

```diff
-const Collapse = ({ collapsed, children }) => {
+const Collapse = ({ collapsed, children }) => {
+ if (collapsed) { return children; } return ( <div> {children} </div> ); };
+    And here is how you would use it:
+    <Collapse> <h1>Hello</h1> <
```

#### Collapse (task/66)

```diff
-const Collapse = ({ collapsed, children }) => {
+const Collapse = ({ collapsed, children }) => {
+ let { children } = this; children.forEach(child => { if (child.isCollapsed) { return; } child.show(); }); this.setProps({ collapsed, children }); }; const Header = ({ children }) =>
```

#### Collapse (task/66)

```diff
-const Collapse = ({ collapsed, children }) => {
+const Collapse = ({ collapsed, children }) => {
+ return isCollapsed ? < div > {children} < / div> : < Collapse isCollapsed = {isCollapsed} expanded = {false} > {children} < / Collapse>; }; const Button = ({ label,
```

#### Collapse (task/66)

```diff
-const Collapse = ({ collapsed, children }) => {
+const Collapse = ({ collapsed, children }) => {
+ if (collapsed) { return null; } return ( <div> {children} </div> ); }; const rowCount = ({ children }) => { return children.map(i => <div key={i}> {i} </
```

#### Collapse (task/66)

```diff
-const Collapse = ({ collapsed, children }) => {
+const Collapse = ({ collapsed, children }) => {
+
+    const hasChildren = children.length > 0
+    return (
+    <div className={`collapse ${hasChildren ? 'show' : 'hide'}`}>
+    {!collapsed && children}
```

#### RippleButton (task/67)

```diff
-const RippleButton = ({ children, onClick }) => {
+const RippleButton = ({ children, onClick }) => {
+
+    return (
+    <RippleButton label="Press Me" onClick={onClick}>
+    {children}
+    </RippleButton>
+    );
+    };
+    // Left-aligned RippleButton
```

#### RippleButton (task/67)

```diff
-const RippleButton = ({ children, onClick }) => {
+const RippleButton = ({ children, onClick }) => {
+ return ( <TouchableOpacity onPress={onClick}> <View style={styles.ripple}> <Text style={styles.rippleText}>{children}</Text> </View> </TouchableOpacity>
```

#### RippleButton (task/67)

```diff
-const RippleButton = ({ children, onClick }) => {
+const RippleButton = ({ children, onClick }) => {
+ return ( <TouchableOpacity onPress={onClick}> <View style={styles.ripple}> {children} </View> </TouchableOpacity> ); }; var styles = StyleSheet.create({ ripple: {
```

#### RippleButton (task/67)

```diff
-const RippleButton = ({ children, onClick }) => {
+const RippleButton = ({ children, onClick }) => {
+ return ( <TouchableOpacity onPress={onClick}> <View style={styles.ripple}> <CircleAvatar size={30} color="#ffa51a" /> <Text style={styles.rippleText
```

#### RippleButton (task/67)

```diff
-const RippleButton = ({ children, onClick }) => {
+const RippleButton = ({ children, onClick }) => {
+ return ( <div onClick={onClick}> {children} </div> ); };
+    Passing Children
+    In the example above, we passed children in via the second argument of the JSX function. This will pass the first
```

#### useMutationObserver (task/68)

```diff
-const useMutationObserver = (
+const useMutationObserver = (
+() => { let { parent , child , mutation } = useWindow ; return function () { return parent . observe ( child , mutation ); }; })();
+    I've also modified this code to use a more powerful API that lets you pass
```

#### useMutationObserver (task/68)

```diff
-const useMutationObserver = (
+const useMutationObserver = (
+ target , /* callback */ ) => { const observer = new MutationObserver ( observerCallback ); observer . observe ( target , { subtree : true , childList : true }); return observer ; }; const observeMutation = async ( target ,
```

#### useMutationObserver (task/68)

```diff
-const useMutationObserver = (
+const useMutationObserver = (
+ ) => { const root = document . querySelector ( '#root' ) ; const observer = new MutationObserver ( ( mutations ) => { mutations . forEach ( ( mutation ) => { mutation . addedNodes . forEach
```

#### useMutationObserver (task/68)

```diff
-const useMutationObserver = (
+const useMutationObserver = (
+ ) => { if ( ! window . mutationObserver ) { window . mutationObserver = new MutationObserver ( ( mutations ) => { for ( const mutation of mutations ) { const mutationTarget = mutation . target ; if ( mutationTarget
```

#### useMutationObserver (task/68)

```diff
-const useMutationObserver = (
+const useMutationObserver = (
+ fn ) => { const node = target . querySelector ( ' .js-mutation-observer-target ' ); const observer = new MutationObserver (fn); return observer . observe (node, { childList : true ,
```

#### Tooltip (task/69)

```diff
-const Tooltip = ({ children, text, ...rest }) => {
+const Tooltip = ({ children, text, ...rest }) => {
+
+    const style = {
+    position: 'absolute',
+    backgroundColor: `rgb(${rgb.hexToRgb(text)}), ${rgb.hexToRgb(text)}`,
+    borderRad
```

#### Tooltip (task/69)

```diff
-const Tooltip = ({ children, text, ...rest }) => {
+const Tooltip = ({ children, text, ...rest }) => {
+
+    const content = children && children . map ( child => child . node . content ) || [];
+    return (
+    < div className = { ` tooltip ${ styles . tooltip } ` } >
+    < div className =
```

#### Tooltip (task/69)

```diff
-const Tooltip = ({ children, text, ...rest }) => {
+const Tooltip = ({ children, text, ...rest }) => {
+ const { html, css } = this.props; const content = html`<div class="tooltip ${css.tooltip}" ${css.tooltipShadow}>${text}</div>`; return ( <div
```

#### Tooltip (task/69)

```diff
-const Tooltip = ({ children, text, ...rest }) => {
+const Tooltip = ({ children, text, ...rest }) => {
+
+    let textSplit = text.split(/\s+/);
+    let wrapper = document.createElement('div');
+    wrapper.className = 'tooltip';
+    let inputStyle = {
+    'color
```

#### Tooltip (task/69)

```diff
-const Tooltip = ({ children, text, ...rest }) => {
+const Tooltip = ({ children, text, ...rest }) => {
+ const { icon, icon_class, style, ...rest } = rest return ( <div className={style}> <div className={style}><span>{text}</span></div> <span className={style}
```

#### useTimeout (task/70)

```diff
-const useTimeout = (callback, delay) => {
+const useTimeout = (callback, delay) => {
+
+    return new Promise((resolve, reject) => {
+    setTimeout(() => {
+    if (callback()) {
+    resolve(true);
+    } else {
+    reject(false);
+    }
```

#### useTimeout (task/70)

```diff
-const useTimeout = (callback, delay) => {
+const useTimeout = (callback, delay) => {
+
+    const id = setTimeout(() => {
+    callback();
+    }, delay);
+    return () => clearTimeout(id);
+    };
+    const event = {};
+    The useTimeout function accepts two arguments,
```

#### useTimeout (task/70)

```diff
-const useTimeout = (callback, delay) => {
+const useTimeout = (callback, delay) => {
+
+    let timeout
+    const cancel = () => {
+    clearTimeout(timeout)
+    callback()
+    }
+    setTimeout(() => {
+    cancel()
+    callback()
+    }, delay)
```

#### useTimeout (task/70)

```diff
-const useTimeout = (callback, delay) => {
+const useTimeout = (callback, delay) => {
+ return new Promise((resolve, reject) => { if (delay <= 0) { return reject(new Error('Request took too long')) } setTimeout(() => { resolve(callback()) }, delay) }) }
+    We need
```

#### useTimeout (task/70)

```diff
-const useTimeout = (callback, delay) => {
+const useTimeout = (callback, delay) => {
+
+    let timeoutId;
+    let timeout;
+    if (delay) {
+    timeoutId = setTimeout(() => {
+    callback();
+    timeout = null;
+    }, delay);
+    } else {
```

#### useError (task/71)

```diff
-const useError = err => {
+const useError = err => {
+
+    console.error(err);
+    return Promise.reject(err);
+    };
+    ...
+    }
+    
+    const doSomethingAsync = () => {
+    return new Promise((resolve, reject) =>
```

#### useError (task/71)

```diff
-const useError = err => {
+const useError = err => {
+ throw new Error(err); });
+    Use of for...of
+    ES6 includes a new for...of loop, which is more useful for iterating over arrays and arrays-like objects than the traditional for...in loop.
```

#### useError (task/71)

```diff
-const useError = err => {
+const useError = err => {
+
+    if (err) {
+    throw new Error(err);
+    }
+    }
+    const getUser = () => {
+    return usePromise(userService.getUser())
+    .then(user =>
```

#### useError (task/71)

```diff
-const useError = err => {
+const useError = err => {
+
+    console.error(err);
+    process.exit(1);
+    };
+    const handleError = err => {
+    if (err.code === 'EADDRINUSE') {
+    useError(err
```

#### useError (task/71)

```diff
-const useError = err => {
+const useError = err => {
+
+    // do something
+    throw err;
+    };
+    const makeError = err => new Error(`${err.message}`);
+    const makeUseError = err => {
+    useError(err);
```

#### useCopyToClipboard (task/72)

```diff
-const useCopyToClipboard = text => {
+const useCopyToClipboard = text => {
+
+    const selection = document.selection ? document.selection.createRange() : false;
+    selection.text = text;
+    const promise = document.execCommand("copy");
+    return promise;
+    };
+    const
```

#### useCopyToClipboard (task/72)

```diff
-const useCopyToClipboard = text => {
+const useCopyToClipboard = text => {
+ const htmlText = text . toString (). trim (); if ( ! htmlText ) { return false ; } // Use "process" to convert the html string to a Uint8Array of // `const u8` since that type is required
```

#### useCopyToClipboard (task/72)

```diff
-const useCopyToClipboard = text => {
+const useCopyToClipboard = text => {
+ let plainText = text . toString (); let unformattedText = plainText . replace ( /
+    /g , ' ' ). replace ( /\r/g , ' ' ); let formattedText = unformattedText . replace
```

#### useCopyToClipboard (task/72)

```diff
-const useCopyToClipboard = text => {
+const useCopyToClipboard = text => {
+
+    const dataURI = new DataURI(text);
+    const fragment = document.createDocumentFragment();
+    fragment.appendChild(dataURI.fragment);
+    fragment.querySelector(
```

#### useCopyToClipboard (task/72)

```diff
-const useCopyToClipboard = text => {
+const useCopyToClipboard = text => {
+
+    const textArea = document.getElementById('textArea');
+    textArea.value = text;
+    textArea.focus();
+    return () => {
+    textArea.select();
+    textArea.scroll
```

#### useMap (task/73)

```diff
-const useMap = initialValue => {
+const useMap = initialValue => {
+
+    const uninitialized = new Map ();
+    const update = ( key , value ) => {
+    uninitialized . set ( key , value );
+    return uninitialized ;
+    };
+    return ( map ) => {
```

#### useMap (task/73)

```diff
-const useMap = initialValue => {
+const useMap = initialValue => {
+ const result = initialValue ; if ( state . isLoading ) { result = { ... result , loading : true } ; } else if ( state . isFetching ) { result = { ... result , loading : true } ; } return
```

#### useMap (task/73)

```diff
-const useMap = initialValue => {
+const useMap = initialValue => {
+ const newValue = useMap(initialValue); return newValue; }; const run = useMap(run);
+    useMemo
+    useMemo(fn, args, initialValue)
+    Use memoized version of the supplied
```

#### useMap (task/73)

```diff
-const useMap = initialValue => {
+const useMap = initialValue => {
+ const newMap = new Map (); newMap . set ( initialValue , initialValue ); return newMap ; }; const useWeakMap = initialValue => { const newMap = new WeakMap (); newMap . set ( initialValue , initialValue
```

#### useMap (task/73)

```diff
-const useMap = initialValue => {
+const useMap = initialValue => {
+
+    const map = new Map ();
+    for ( const [ key , value ] of initialValue) {
+    map . set (key, value);
+    }
+    return map;
+    };
+    /**
+    *
```

#### AutoLink (task/74)

```diff
-const AutoLink = ({ text }) => {
+const AutoLink = ({ text }) => {
+ if (text.length <= 2) { return false; } return text.slice(0, 2).toLowerCase() === 'http'; }; const isInLink = (el, arr) => arr.includes(el); const is
```

#### AutoLink (task/74)

```diff
-const AutoLink = ({ text }) => {
+const AutoLink = ({ text }) => {
+ const text = text.toLowerCase(); return text.match(/\blink$|\bno-link$|\bbig\b/); };
+    // To use the AutoLinker, import it and call the
```

#### AutoLink (task/74)

```diff
-const AutoLink = ({ text }) => {
+const AutoLink = ({ text }) => {
+ return < div > < span > { text } </ span > </ div > } const Link = ({ url }) => { return < a href = { url } > { text } </ a > } const LinkAuto = ({ url }) => <
```

#### AutoLink (task/74)

```diff
-const AutoLink = ({ text }) => {
+const AutoLink = ({ text }) => {
+ const link = new IntersectionObserver(observer => { observer.observe(document.querySelector('body'), { childList: true, subtree: true }); observer.disconnect(); }) link.observe(
```

#### AutoLink (task/74)

```diff
-const AutoLink = ({ text }) => {
+const AutoLink = ({ text }) => {
+ let potentialLinks = text. split ( / [ \s\S ] +/ ) . filter ( text => text ) return potentialLinks . reduce (( last , current ) => { if ( current . length < 3 ) { return last } return
```

#### useDebounce (task/75)

```diff
-const useDebounce = (value, delay) => {
+const useDebounce = (value, delay) => {
+ let callback = null if (delay > 0) { setTimeout(() => { callback = () => { if (isNaN(value) || value < 0) { stopDebounce(callback) } else { setTimeout(() =>
```

#### useDebounce (task/75)

```diff
-const useDebounce = (value, delay) => {
+const useDebounce = (value, delay) => {
+ let currentValue = 0; const debouncedValue = (event) => { if (currentValue !== value) { currentValue = value; } return event.target.value; }; return debouncedValue; }; export default useDebounce
```

#### useDebounce (task/75)

```diff
-const useDebounce = (value, delay) => {
+const useDebounce = (value, delay) => {
+
+    let [prev, set] = useState(value)
+    return function debounce(callback) {
+    const [prev, set] = useState(value)
+    if (prev !== set) {
```

#### useDebounce (task/75)

```diff
-const useDebounce = (value, delay) => {
+const useDebounce = (value, delay) => {
+
+    return value
+    .debounce(delay, _.debounce(update, 1000))
+    .map(value => {
+    return { ...value, status: true };
+    });
+    };
```

#### useDebounce (task/75)

```diff
-const useDebounce = (value, delay) => {
+const useDebounce = (value, delay) => {
+
+    return new Promise((resolve, reject) => {
+    setTimeout(() => {
+    if (value !== prev) {
+    prev = value;
+    resolve(prev);
+    }
+    },
```

#### useFetch (task/76)

```diff
-const useFetch = (url, options) => {
+const useFetch = (url, options) => {
+ return new Promise((resolve, reject) => { fetch(url, options).then(res => { resolve(res.text()); }).catch(reject); }); };
+    Conclusion
+    Working with async/await is a
```

#### useFetch (task/76)

```diff
-const useFetch = (url, options) => {
+const useFetch = (url, options) => {
+ return request(url, options) .then(response => response.json()) .then(json => { if (json.success) { return json.payload } return null }) .catch(error => { return null }) }
```

#### useFetch (task/76)

```diff
-const useFetch = (url, options) => {
+const useFetch = (url, options) => {
+ let config = { method: 'GET', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' } }; return fetch(url, config) .then(response => response.json()) .then
```

#### useFetch (task/76)

```diff
-const useFetch = (url, options) => {
+const useFetch = (url, options) => {
+ options.headers.set('Accept', 'application/json') if (url.indexOf('?') === -1) { url += '?' } options.query = url } return (select) => { const fetch = useFetch
```

#### useFetch (task/76)

```diff
-const useFetch = (url, options) => {
+const useFetch = (url, options) => {
+
+    const id = Object.assign({}, options.data, {
+    _id: url.id
+    });
+    return new Promise((resolve, reject) => {
+    axios.get(url).then
```

#### useOnGlobalEvent (task/77)

```diff
-const useOnGlobalEvent = (type, callback, options) => {
+const useOnGlobalEvent = (type, callback, options) => {
+ if (typeof options === 'undefined') { options = { context: this }; } let target = { event: event, topic: topic, payload: payload }; // if the item already has a custom handler, we'll call it if
```

#### useOnGlobalEvent (task/77)

```diff
-const useOnGlobalEvent = (type, callback, options) => {
+const useOnGlobalEvent = (type, callback, options) => {
+
+    let next = null;
+    if (options.all) {
+    next = this.globalEvents.next(type, callback, options);
+    } else {
+    const key = options.getKey || type;
```

#### useOnGlobalEvent (task/77)

```diff
-const useOnGlobalEvent = (type, callback, options) => {
+const useOnGlobalEvent = (type, callback, options) => {
+ const eventHandler = options.eventHandler; const eventType = options.eventType; const wrapper = document.createElement('div'); wrapper.className = 'statue-in-use'; wrapper.addEventListener(eventType,
```

#### useOnGlobalEvent (task/77)

```diff
-const useOnGlobalEvent = (type, callback, options) => {
+const useOnGlobalEvent = (type, callback, options) => {
+
+    - this.router.on(`global-event-${type}`, options.useOnGlobalEvent, callback);
+    -};
+    -
+    -exports.useOnGlobalEvent = useOnGlobalEvent
```

#### useOnGlobalEvent (task/77)

```diff
-const useOnGlobalEvent = (type, callback, options) => {
+const useOnGlobalEvent = (type, callback, options) => {
+
+    if (typeof options === 'function') {
+    callback = options;
+    options = {};
+    }
+    if (type === 'browser:navigate') {
+    options.main = type;
```

